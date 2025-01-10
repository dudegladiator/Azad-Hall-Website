from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ContactForm, CommentForm
from django.core.mail import BadHeaderError, send_mail
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from openpyxl import load_workbook
from datetime import datetime, timedelta
from django.contrib import messages
from django.core.paginator import Paginator, Page
from django.views.decorators.csrf import csrf_protect
from datetime import datetime


allowedEmails = [
    "harsh247gupta@gmail.com",
    "harsh90731@gmail.com",
    "rajumeshram767@gmail.com",
    "hariomk628@gmail.com",
    "sg06959.sgsg@gmail.com",
    "pooniakushagra20@gmail.com",
    "somnathmishra1802@gmail.com",
]
allowedEmailsLibrary = [
    "harsh247gupta@gmail.com",
    "pooniakushagra20@gmail.com",
    "harsh90731@gmail.com",
    "rajumeshram767@gmail.com",
    "hariomk628@gmail.com",
    "sg06959.sgsg@gmail.com",
    "pranjalchouhan2014@gmail.com",
    "somnathmishra1802@gmail.com",
]


def import_from_excel(request):
    if request.method == "POST":
        excel_file = request.FILES["excel_file"]
        wb = load_workbook(excel_file)
        ws = wb.active

        azad_boarders_to_create = []

        for row in ws.iter_rows(values_only=True):
            roll_no, name, email, number = row
            azad_boarder = azad_boarders(
                name=name, roll_no=roll_no, emails=email, contact=number, books=0
            )
            azad_boarders_to_create.append(azad_boarder)

        # Use bulk_create to create objects in bulk
        azad_boarders.objects.bulk_create(azad_boarders_to_create)

        return render(request, "index.html")


# For books
def importBooksFromExcel(request):
    if request.method == "POST":
        excel_file = request.FILES["excel_file"]
        wb = load_workbook(excel_file)
        ws = wb.active

        books_to_create = []

        for row in ws.iter_rows(values_only=True):
            book1 = book(
                title=row[0],
                author=row[1],
                department=row[2],
                shelf=row[3],
                quantity=row[4],
                available=row[4],
            )
            books_to_create.append(book1)

        # Use bulk_create to create objects in bulk
        book.objects.bulk_create(books_to_create)

        return render(request, "index.html")


def alumni(request):
    return render(request, "alumni.html")

def addBooks(request):
    if request.user.is_authenticated:
        email = request.user.email
        if email in allowedEmails:
            return render(request, "addBooks.html")
    messages.info(request, "Please login with valid ID to add boarders")
    return redirect("/")


def addBoarders(request):
    if request.user.is_authenticated:
        email = request.user.email
        if email in allowedEmails:
            return render(request, "addBoarders.html")
    messages.info(request, "Please login with valid ID to add boarders")
    return redirect("/")


def login(request):
    return render(request, "login.html")


def index(request):
    if request.user.is_authenticated:
        email = request.user.email
        boarders = azad_boarders.objects.all()
        for boarder in boarders:
            if boarder.emails == email:
                name = boarder.name
                params = {"name": name}
                return render(request, "index.html", params)
        logout(request)
        message = "Please login with valid EmailID"
        params = {"message": message}
        return render(request, "index.html", params)

    return render(request, "index.html")


@csrf_protect
def complain(request):
    if request.user.is_authenticated:
        return render(request, "complain.html")

@csrf_protect
def profile(request):
    if request.method == "POST" and 1:
        boarder = azad_boarders.objects.get(emails=request.user.email)
        if boarder:
            contact_no = request.POST.get("contact")
            name = request.POST.get("name")
            roll_no = request.POST.get("roll_no")
            register = azad_boarders.objects.update(
                roll_no=roll_no,
                name=name,
                contact=contact_no,
            )
            messages.info(request, "Saved Successfully")
            return redirect("/profile")
        else:
            messages.info(request, "Email not found")
    
    boarder = azad_boarders.objects.get(emails=request.user.email)
    return render(request, "profile.html", {"user":boarder})

@csrf_protect
def submit_form(request):
    if request.method == "POST" and request.user.is_authenticated:
        category = request.POST.get("category")
        room_no = request.POST.get("room_no")
        complain = request.POST.get("complain")
        contact_no = request.POST.get("contact_no")
        # image = request.FILES.get('image')
        image_link = request.POST.get("image")
        boarder = azad_boarders.objects.get(emails=request.user.email)
        name = boarder.name
        email = boarder.emails
        roll_no = boarder.roll_no
        now = datetime.now()
        t_string = now.strftime("%d/%m/%Y %H:%M %p")
        created_at = t_string
        register = complaints.objects.create(
            name=name,
            roll_no=roll_no,
            email=email,
            category=category,
            contact_no=contact_no,
            complain=complain,
            status="pending",
            room_no=room_no,
            created_at=created_at,
            image_link=image_link,
            review="None",
        )
        # Return a response (you can render a template or return a JSON response)
        # message="Complain submitted successfully!"
        # params={"message":message,"name":name}
        messages.info(request, "Complain submitted successfully")
        # return render(request, 'index.html')
        return redirect("/")
    else:
        # Handle GET requests or other methods if necessary
        return HttpResponse("Invalid request method")


def showComplaints(request):
    if request.user.is_authenticated:
        email = request.user.email
        if email in allowedEmails:
            pending_complaints = complaints.objects.filter(status="pending")
            pending_paginator = Paginator(pending_complaints, 10)
            current_page_pending = pending_paginator.page(
                request.GET.get("pending_page", 1)
            )

            completed_complaints = complaints.objects.filter(
                status="Completed"
            ).order_by("-id")
            completed_paginator = Paginator(completed_complaints, 10)
            current_page_completed = completed_paginator.page(
                request.GET.get("completed_page", 1)
            )

            ongoing_complaints = complaints.objects.filter(status="Ongoing")
            ongoing_paginator = Paginator(ongoing_complaints, 10)
            current_page_ongoing = ongoing_paginator.page(
                request.GET.get("ongoing_page", 1)
            )

            params = {
                "pending_complaints": current_page_pending,
                "completed_complaints": current_page_completed,
                "ongoing_complaints": current_page_ongoing,
            }
            return render(request, "showComplaints.html", params)
    messages.info(request, "Please login with valid ID to access complaints")
    return redirect("/")


def showFullComplain(request, complain_id):
    if request.user.is_authenticated:
        complain = complaints.objects.get(id=complain_id)
        params = {"complain": complain}
        return render(request, "fullComplain.html", params)


def updateStatus(request):
    if request.method == "POST":
        id = request.POST.get("id")
        manager_review = request.POST.get("manager_review")
        set_status = request.POST.get("set_status")
        print(set_status)
        if manager_review == "":
            manager_review = "None"
        complain = complaints.objects.get(id=id)
        if complain.status == "Ongoing":
            complain.status = "Completed"
        else:
            if set_status == "ongoing":
                complain.status = "Ongoing"
            else:
                complain.status = "Completed"
        # if(complain.status=="pending"):
        #     complain.status="Ongoing"
        # else:
        #     complain.status="Completed"
        complain.manager_review = manager_review
        now = datetime.now()
        t_string = now.strftime("%d/%m/%Y %H:%M %p")
        complain.modified_at = t_string
        complain.save()
    return redirect("/showComplaints")


def complain_status(request):
    if request.user.is_authenticated:
        complains = complaints.objects.filter(email=request.user.email).order_by("-id")
        print(complains)
        params = {"complains": complains}
        return render(request, "complain_status.html", params)


def noticeboard(request):
    noticeboard = Notice.objects.all()
    return render(request, "noticeboard.html", {"noticeboard": noticeboard})


def notice(request, noticeid):
    notice = Notice.objects.filter(id=noticeid)
    noticeboard = Notice.objects.all()
    return render(
        request, "notice.html", {"notice": notice[0], "noticeboard": noticeboard}
    )


def achievements(request):
    achievements = Achievements.objects.all()
    return render(request, "achievements.html", {"achievements": achievements})


def achievement(request, achievementid):
    achievement = Achievements.objects.filter(id=achievementid)
    achievements = Achievements.objects.all()
    return render(
        request,
        "achievement.html",
        {"achievement": achievement[0], "achievements": achievements},
    )


def events(request):
    events = Event.objects.all()
    return render(request, "events.html", {"events": events})


def khoj(request):
    return render(request, "khoj.html")


def library(request, searchedBooks=None, str=None):
    if request.user.is_authenticated:
        if searchedBooks:
            books = searchedBooks
            return render(
                request, "library.html", {"books": books, "searchedString": str}
            )
        else:
            books = book.objects.all().order_by("id")
        books_paginator = Paginator(books, 30)
        current_page_books = books_paginator.page(request.GET.get("books_page", 1))
        # message=None
        # if checkout:
        #     message="Request submitted successfully"
        return render(
            request,
            "library.html",
            {"books": current_page_books, "searchedString": str},
        )
    messages.info(request, "Please login with valid ID to access library")
    return redirect("/")


def checkout(request):
    if request.method == "POST":
        id = request.POST.get("id")
        Book = book.objects.get(id=id)
        boarder = azad_boarders.objects.get(emails=request.user.email)
        if boarder.books < 2:
            now = datetime.now()
            boarder.books += 1
            t_string = now.strftime("%d/%m/%Y %H:%M %p")
            requestedBook.objects.create(
                title=Book.title,
                author=Book.author,
                department=Book.department,
                shelf=Book.shelf,
                studentName=boarder.name,
                studentRoll_no=boarder.roll_no,
                email=boarder.emails,
                created_at=t_string,
                status="requested",
                bookID=id,
            )
            x = Book.available
            Book.available = x - 1
            Book.save()
            boarder.save()
        else:
            messages.info(request, "You can only apply for 2 books at a time")
            return redirect("/library")

        # print(book)
        # messages.info(request, "Request submitted successfully")
        messages.info(request, "Request submitted successfully")
        return redirect("/library")


def checkedOutBooks(request):
    if request.user.is_authenticated and request.user.email in allowedEmailsLibrary:
        now = datetime.now()
        books = requestedBook.objects.all()
        for Rbook in books:
            b = Rbook.created_at[0:10]
            a = datetime.strptime(b, "%d/%m/%Y")
            print((now - a).days)
            if (now - a).days > 3:
                boarder = azad_boarders.objects.get(emails=Rbook.email)
                boarder.books -= 1
                boarder.save()
                Book = book.objects.get(id=Rbook.bookID)
                Book.available += 1
                Book.save()
                Rbook.delete()
        requestedBooks = requestedBook.objects.filter(status="requested")
        requestedBooks_paginator = Paginator(requestedBooks, 10)
        current_page_requestedBooks = requestedBooks_paginator.page(
            request.GET.get("requestedBooks_page", 1)
        )

        checkedOutBooks = requestedBook.objects.filter(status="checkedOut")
        checkedOutBooks_paginator = Paginator(checkedOutBooks, 10)
        current_page_checkedOutBooks = checkedOutBooks_paginator.page(
            request.GET.get("checkedOutBooks_page", 1)
        )

        return render(
            request,
            "checkedOutBooks.html",
            {
                "requestedBooks": current_page_requestedBooks,
                "checkedOutBooks": current_page_checkedOutBooks,
            },
        )
    messages.info(request, "Please login with valid ID to access library records")
    return redirect("/")


def previousBookRequests(request):
    if request.user.is_authenticated:
        requestedBooks = requestedBook.objects.filter(
            status="requested", email=request.user.email
        )
        requestedBooks_paginator = Paginator(requestedBooks, 10)
        current_page_requestedBooks = requestedBooks_paginator.page(
            request.GET.get("requestedBooks_page", 1)
        )

        checkedOutBooks = requestedBook.objects.filter(
            status="checkedOut", email=request.user.email
        )
        checkedOutBooks_paginator = Paginator(checkedOutBooks, 10)
        current_page_checkedOutBooks = checkedOutBooks_paginator.page(
            request.GET.get("checkedOutBooks_page", 1)
        )

        return render(
            request,
            "previousBookRequests.html",
            {
                "requestedBooks": current_page_requestedBooks,
                "checkedOutBooks": current_page_checkedOutBooks,
            },
        )
    messages.info(request, "Please login with valid ID to access library records")
    return redirect("/")


def approve(request):
    if request.user.is_authenticated and request.user.email in allowedEmailsLibrary:
        if request.method == "POST":
            id = request.POST.get("id")
            Book = requestedBook.objects.get(id=id)
            Book.status = "checkedOut"
            now = datetime.now()
            t_string = now.strftime("%d/%m/%Y %H:%M %p")
            Book.created_at = t_string
            Book.save()
            return redirect("/checkedOutBooks")


def checkIn(request):
    if request.user.is_authenticated and request.user.email in allowedEmailsLibrary:
        if request.method == "POST":
            id = request.POST.get("id")
            RequestedBook = requestedBook.objects.get(id=id)
            Book = book.objects.get(id=RequestedBook.bookID)
            Book.available += 1
            Book.save()
            boarder = azad_boarders.objects.get(emails=RequestedBook.email)
            boarder.books -= 1
            boarder.save()
            RequestedBook.delete()
            return redirect("/checkedOutBooks")


def cancelBookRequest(request):
    id = request.POST.get("id")
    RequestedBook = requestedBook.objects.get(id=id)
    boarder = azad_boarders.objects.get(emails=RequestedBook.email)
    boarder.books -= 1
    boarder.save()
    Book = book.objects.get(id=RequestedBook.bookID)
    Book.available += 1
    Book.save()
    RequestedBook.delete()
    return redirect("/previousBookRequests")


def search(request):
    if request.method == "POST":
        str = request.POST.get("search")

        if str:
            books = book.objects.filter(
                models.Q(title__icontains=str)
                | models.Q(author__icontains=str)
                | models.Q(department__icontains=str)
            )
            if books:
                return library(request, books, str)
            else:
                books = book.objects.all()
                messages.info(request, "No books found")
                return redirect("/library")

    books = book.objects.all()
    # messages.info(request, 'No books found')
    return redirect("/library")


def about(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
        subject = request.POST.get("subject", "")
        message = request.POST.get("msg", "")
        from_email = request.POST.get("email", "")
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ["smarakdev@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("/about")
        else:
            form = ContactForm()
            return render(request, "about.html", {"form": form})
    else:
        form = ContactForm()
        return render(request, "about.html", {"form": form})


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def postComment(request):
    # request should be ajax and method should be POST.
    print("hello")
    if is_ajax(request=request) and request.method == "POST":
        # get the form data
        form = CommentForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                ],
            )
            # send to client side.
            print("saved")
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def event(request, eventid):
    id = eventid
    # print("message", eventid)
    event = Event.objects.filter(id=eventid)
    itemlist = []
    # print(event)
    # print(event[0].para_set.all())
    commentform = CommentForm()
    comments = event[0].comments.all()

    cover = ""
    for item in event[0].imagemodel_set.all():
        if item.caption == "cover":
            cover = item
            continue
        itemlist.append(item)
    for item in event[0].para_set.all():
        itemlist.append(item)
    # print(itemlist)
    itemlist.sort(key=lambda x: x.date, reverse=True)
    # print(itemlist)
    # print(cover.caption)
    events = Event.objects.all()
    return render(
        request,
        "event.html",
        {
            "events": events,
            "cover": cover,
            "event": event[0],
            "form": commentform,
            "comments": comments,
        },
    )


def custom_logout(request):
    logout(request)
    message = "Logged out successfully"
    params = {"message": message}
    return render(request, "index.html", params)

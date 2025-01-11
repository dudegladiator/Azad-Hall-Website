from django.urls import path, include
from django.contrib.auth.views import logout_then_login
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("event/<int:eventid>", views.event, name="event"),
    path("events", views.events, name="events"),
    path("noticeboard", views.noticeboard, name="noticeboard"),
    path("notice/add", views.noticeadd, name="add_notice"),
    path("achievement/<int:achievementid>", views.achievement, name="achievement"),
    path("achievements", views.achievements, name="achievements"),
    path("about", views.about, name="about"),
    path("post/comment", views.postComment, name="post_comment"),
    path("login", views.login, name="login"),
    path("", include("allauth.urls")),
    path("accounts/", include("allauth.urls")),
    path("custom_logout", views.custom_logout, name="custom_logout"),
    path("addBoarders", views.addBoarders, name="addBoarders"),
    path("importFromExcel", views.import_from_excel, name="importFromExcel"),
    path("complain", views.complain, name="complain"),
    path("submit", views.submit_form, name="submit_form"),
    path("showComplaints", views.showComplaints, name="showComplaints"),
    path("updateStatus", views.updateStatus, name="updateStatus"),
    path("complain_status", views.complain_status, name="complain_status"),
    path("fullComplain/<int:complain_id>", views.showFullComplain, name="fullComplain"),
    path("khoj", views.khoj, name="khoj"),
    path("library", views.library, name="library"),
    path("checkout", views.checkout, name="checkout"),
    path("checkedOutBooks", views.checkedOutBooks, name="checkedOutBooks"),
    path("approve", views.approve, name="approve"),
    path("checkIn", views.checkIn, name="checkIn"),
    path("search", views.search, name="search"),
    path(
        "importBooksFromExcel", views.importBooksFromExcel, name="importBooksFromExcel"
    ),
    path("addBooks", views.addBooks, name="addBooks"),
    path(
        "previousBookRequests", views.previousBookRequests, name="previousBookRequests"
    ),
    path("cancelBookRequest", views.cancelBookRequest, name="cancelBookRequest"),
    path("alumni", views.alumni, name="alumni"),
    path('user_form', views.user_form_view, name='user_form'),
    path("profile", views.profile, name="profile"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

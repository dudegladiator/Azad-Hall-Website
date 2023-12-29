from django.db import models
from datetime import datetime

# Create your models here.

class azad_boarders(models.Model):
    roll_no=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    emails=models.EmailField()
    contact=models.CharField(max_length=12, null=True)
    books=models.IntegerField(default=0)
    
class complaints(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.CharField(max_length=15)
    category = models.CharField(max_length=20, default="mess")
    email=models.EmailField()
    contact_no=models.CharField(max_length=12, null=True)
    room_no=models.CharField(max_length=5)
    complain=models.CharField(max_length=500)
    status=models.CharField(max_length=10)
    review=models.CharField(max_length=250, default=None,null=True)
    created_at=models.CharField(max_length=20)
    modified_at=models.CharField(max_length=20)
    manager_review=models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='complain_images', null=True)  # You can specify the upload path

class book(models.Model):
    title=models.CharField(max_length=50, null=True)
    author=models.CharField(max_length=50, null=True)
    department=models.CharField(max_length=20, null=True)
    shelf=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    available=models.IntegerField(null=True)

class requestedBook(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    department=models.CharField(max_length=20, null=True)
    shelf=models.IntegerField(null=True)
    studentName=models.CharField(max_length=50)
    studentRoll_no=models.CharField(max_length=15)
    email=models.EmailField()
    created_at=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    bookID=models.IntegerField(null=True)

class Event(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', default='static/images/logo/logo.svg')
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return (self.title)


class Para(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return (self.text)

    @property
    def type(self):
        return "para"


class Imagemodel(models.Model):
    caption = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='azad/static/img/', null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return (self.caption)

    @property
    def static_url(self):
        "Returns the url to be used in templates"
        return ((self.image.url)[12:])

    @property
    def type(self):
        "Returns the url to be used in templates"
        return "image"


class Coveritem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.OneToOneField(Imagemodel,
                                 on_delete=models.CASCADE,
                                 primary_key=True,)


class Notice(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', default='static/images/logo/logo.svg')
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return (self.title)


class Achievements(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', default='static/images/logo/logo.svg')
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return (self.title)


class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Team(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    dept = models.CharField(max_length=250)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=400)
    msg = models.TextField()

    def __str__(self):
        return (self.name)


class Comment(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

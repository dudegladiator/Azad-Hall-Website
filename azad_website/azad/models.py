from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class azad_boarders(models.Model):
    roll_no=models.CharField(max_length=15)
    name=models.CharField(max_length=500)
    emails=models.EmailField()
    contact=models.CharField(max_length=12, null=True)
    books=models.IntegerField(null=True)
    role=models.CharField(max_length=500)
    
class complaints(models.Model):
    name=models.CharField(max_length=500)
    roll_no=models.CharField(max_length=15)
    category = models.CharField(max_length=200)
    email=models.EmailField()
    contact_no=models.CharField(max_length=12, null=True)
    room_no=models.CharField(max_length=5)
    complain=models.CharField(max_length=500)
    status=models.CharField(max_length=100)
    review=models.CharField(max_length=250, null=True)
    created_at=models.CharField(max_length=200)
    modified_at=models.CharField(max_length=200)
    manager_review=models.CharField(max_length=500, null=True)
    image_link = models.URLField(null=True)

class book(models.Model):
    title = models.CharField(max_length=1000, null=True)
    author = models.CharField(max_length=1000, null=True)
    department = models.CharField(max_length=1000, null=True)
    shelf = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    available = models.IntegerField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author']),
            models.Index(fields=['department']),
        ]


class requestedBook(models.Model):
    title=models.CharField(max_length=500)
    author=models.CharField(max_length=500)
    department=models.CharField(max_length=200, null=True)
    shelf=models.IntegerField(null=True)
    studentName=models.CharField(max_length=500)
    studentRoll_no=models.CharField(max_length=15)
    email=models.EmailField()
    created_at=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    bookID=models.IntegerField(null=True)

class Event(models.Model):
    title = models.CharField(max_length=2000)
    subtitle = models.CharField(max_length=2000)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images', default='static/images/logo/logo.svg')
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return (self.title)


class Para(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return (self.text)

    @property
    def type(self):
        return "para"


class Imagemodel(models.Model):
    caption = models.CharField(max_length=2000)
    description = models.TextField()
    image = models.ImageField(upload_to='azad/static/img/', null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now())

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
    title = models.CharField(max_length=2000)
    description = models.TextField()
    image = models.OneToOneField(Imagemodel,
                                 on_delete=models.CASCADE,
                                 primary_key=True,)


class Notice(models.Model):
    title = models.CharField(max_length=2500)
    subtitle = models.CharField(max_length=2500)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', default='static/images/logo/logo.svg')
    date = models.DateTimeField(default=timezone.now(), blank=True)

    def __str__(self):
        return (self.title)


class Achievements(models.Model):
    title = models.CharField(max_length=2500)
    subtitle = models.CharField(max_length=2500)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', default='static/images/logo/logo.svg')
    date = models.DateTimeField(default=timezone.now(), blank=True)

    def __str__(self):
        return (self.title)


class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Team(models.Model):
    name = models.CharField(max_length=2500)
    title = models.CharField(max_length=2500)
    dept = models.CharField(max_length=2500)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)


class Contact(models.Model):
    name = models.CharField(max_length=2500)
    email = models.EmailField()
    subject = models.CharField(max_length=4000)
    msg = models.TextField()

    def __str__(self):
        return (self.name)


class Comment(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=800)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

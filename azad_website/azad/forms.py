from django import forms
from django.core.validators import RegexValidator
from .models import Contact, Comment, complaints, LibraryDuty


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "msg": forms.Textarea(attrs={"class": "form-control"}),
        }
        widget = forms.FileInput(attrs={"class": "form-control"})


class LibraryDutyForm(forms.ModelForm):
    class Meta:
        model = LibraryDuty
        fields = ['name', 'phone_number', 'time1', 'details', 'time2', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter phone number without country code'}),
            'time1': forms.TimeInput(format='%I:%M %p', attrs={'type': 'time', 'placeholder': 'Enter time (e.g., 02:30 PM)'}),
            'details': forms.Textarea(attrs={'placeholder': 'Enter additional details here', 'rows': 5}),
            'time2': forms.TimeInput(format='%I:%M %p', attrs={'type': 'time', 'placeholder': 'Enter time (e.g., 02:30 PM)'}),
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'Enter date (e.g., 2025-01-11)'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["event", "name", "email", "body"]


class ComplaintForm(forms.ModelForm):
    upload_image = forms.FileField(required=False)

    class Meta:
        model = complaints
        fields = [
            "name",
            "roll_no",
            "category",
            "email",
            "contact_no",
            "room_no",
            "complain",
            "upload_image",
        ]

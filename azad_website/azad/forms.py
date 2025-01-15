from django import forms
from django.core.validators import RegexValidator
from .models import Contact, Comment, complaints


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


class LibraryDutyForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Enter your full name"}),
    )
    phone_number = forms.CharField(
        label="Phone Number",
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.",
            ),
        ],
        widget=forms.TextInput(
            attrs={"placeholder": "Enter phone number without country code"}
        ),
    )
    time1 = forms.TimeField(
        label="Time 1",
        widget=forms.TimeInput(
            format="%I:%M %p",  # 12-hour format with AM/PM
            attrs={"placeholder": "Enter time (e.g., 02:30 PM)", "type": "time"},
        ),
    )
    details = forms.CharField(
        label="Details",
        widget=forms.Textarea(
            attrs={"placeholder": "Enter additional details here", "rows": 5}
        ),
    )
    time2 = forms.TimeField(
        label="Time 2",
        widget=forms.TimeInput(
            format="%I:%M %p",  # 12-hour format with AM/PM
            attrs={"placeholder": "Enter time (e.g., 02:30 PM)", "type": "time"},
        ),
    )
    date = forms.DateField(
        label="Date",
        widget=forms.DateInput(
            format="%Y-%m-%d",
            attrs={"placeholder": "Enter date (e.g., 2025-01-11)", "type": "date"},
        ),
    )


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

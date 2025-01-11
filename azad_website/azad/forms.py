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


class UserForm(forms.Form):
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
            attrs={"placeholder": "Enter phone number with country code"}
        ),
    )
    details = forms.CharField(
        label="Details",
        widget=forms.Textarea(
            attrs={"placeholder": "Enter additional details here", "rows": 5}
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

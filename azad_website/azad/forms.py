from django import forms
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
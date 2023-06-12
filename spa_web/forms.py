from django import forms
from .models import Contact, Project


class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    message = forms.CharField(
        required=False, max_length=200, widget=forms.Textarea(attrs={"rows": "5"})
    )

    class Meta:
        model = Contact
        fields = ("name", "email", "message")


class ProjectForm(forms.Form):
    judul = forms.CharField(required=True)
    thumbnail = forms.ImageField(required=True)
    deskripsi = forms.CharField(required=True, widget=forms.Textarea())

    class Meta:
        model = Project
        fields = ("judul", "thumbnail", "deskripsi")

from django import forms
from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    message = forms.CharField(required=False, max_length=200)

    class Meta:
        model = Contact
        fields = ("name", "email", "message")

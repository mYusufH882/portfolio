from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from .models import Contact


# Create your views here.
def IndexView(request):
    form = ContactForm

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
        else:
            form = ContactForm

        Contact.objects.create(name=name, email=email, message=message)

        messages.success(
            request, "Data berhasil tersimpan!!! Harap tunggu konfirmasi selanjutnya."
        )
        return redirect("index")

    return render(request, "index.html", {"forms": form})

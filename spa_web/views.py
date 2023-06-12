from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import os

from .forms import ContactForm, ProjectForm
from .models import Contact, Project


# Create your views here.
def IndexView(request):
    projects = Project.objects.all()
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

    return render(request, "index.html", {"forms": form, "data": projects})


def DetailView(request, id_projects):
    project = Project.objects.get(pk=id_projects)

    return render(request, "detail.html", {"data": project})


def CreateView(request):
    form = ProjectForm

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            judul = form.cleaned_data["judul"]
            thumbnail = form.cleaned_data["thumbnail"]
            deskripsi = form.cleaned_data["deskripsi"]

            Project.objects.create(
                judul=judul, thumbnail=thumbnail, deskripsi=deskripsi
            )

            messages.success(request, "Projek baru telah ditambahkan!!!")
            return redirect("index")
    else:
        form = ProjectForm()

    return render(request, "forms.html", {"forms": form})


def EditView(request, id_projects):
    try:
        project = Project.objects.get(pk=id_projects)
    except:
        raise HttpResponse("Maaf data proyek tidak ditemukan !!!")

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project.judul = form.cleaned_data["judul"]
            project.thumbnail = form.cleaned_data["thumbnail"]
            project.deskripsi = form.cleaned_data["deskripsi"]
            project.save()

            messages.success(request, "Proyek berhasil diubah!!!")
            return redirect("index")
    else:
        form = ProjectForm(
            initial={
                "judul": project.judul,
                "thumbnail": project.thumbnail,
                "deskripsi": project.deskripsi,
            }
        )

    return render(request, "forms.html", {"forms": form})


def DeleteView(request, id_projects):
    try:
        project = Project.objects.get(pk=id_projects)
        if len(project.thumbnail) > 0:
            os.remove(project.thumbnail.path)

        project.delete()

        messages.success(request, "Proyek telah dihapus!!!")
        return redirect("index")
    except:
        raise HttpResponse("Proyek tidak ditemukan!!!")

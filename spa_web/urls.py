from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("detail/<int:id_projects>", views.DetailView, name="detail"),
    path("buat-projek/", views.CreateView, name="buat-projek"),
    path("edit/<int:id_projects>", views.EditView, name="edit"),
    path("hapus/<int:id_projects>", views.DeleteView, name="hapus"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

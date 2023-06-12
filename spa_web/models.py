from django.db import models
from django.conf import settings


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contacts"


class Project(models.Model):
    judul = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to="image-projects/")
    deskripsi = models.TextField()

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.judul

    @property
    def thumbnail_url(self):
        return (
            "%s%s" % (settings.MEDIA_HOST, self.thumbnail.url) if self.thumbnail else ""
        )

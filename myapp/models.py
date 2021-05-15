from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
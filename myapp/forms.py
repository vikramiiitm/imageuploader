from django import forms
from django.db import models
from django.forms import fields
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model  = Image
        fields = "__all__"
        labels = {'photo':''}
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField


class Category(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

    def get_absolute_url(self):
       return reverse("index")


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    stamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
       return reverse("index")


# Create your models here.

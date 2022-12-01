from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=50)
    Profile_Picture = models.ImageField(upload_to="static/profile/")
    Designation = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
       return reverse("index")
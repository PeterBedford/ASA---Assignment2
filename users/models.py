from distutils.command.upload import upload
from email.headerregistry import Address
from tokenize import Name
from turtle import up
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)
 first_name = models.CharField(max_length=30)
 last_name = models.CharField(max_length=30)
 address = models.CharField(max_length=100)
 City = models.CharField(max_length=30)
 Country = models.CharField(max_length=100)
 Photo = models.ImageField(upload_to='profile_pics')

def __str__(self):
    return str(self.user)

    

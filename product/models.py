from datetime import datetime
from tkinter import CASCADE
from turtle import mode
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):   
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=50)
    average_cost = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50)
    date_released = models.DateField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='product_pics')

    def __str__(self):
        return self.name + ' | ' + self.brand + ' | ' + self.category


class Review(models.Model):

    class Rating(models.IntegerChoices):
        Poor = 1
        Unstatisfactory = 2
        Satisfactory = 3
        Very_Satisfactory = 4
        Outstanding = 5

    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, related_name="Reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices)
    description = models.TextField() 
    date_posted = models.DateField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.Product.name, self.Author)


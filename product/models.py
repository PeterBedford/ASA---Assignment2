from datetime import datetime
from turtle import mode
from unicodedata import category
from django.db import models


class Product(models.Model):   
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=50)
    average_cost = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50)
    date_released = models.DateTimeField(datetime.now())
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='product_pics')

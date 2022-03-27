from pyexpat import model
from re import template
from statistics import mode
from django.shortcuts import render
from django.views.generic import DetailView
from product.models import Product

class ProductView(DetailView):
    model = Product
    template_name = 'products/product.html'


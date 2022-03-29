import re
from django.shortcuts import render
from django.http import HttpResponse
from product.views import ProductView

def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')
    #add email view method here
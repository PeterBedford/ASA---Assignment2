from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #home page
    path('about', views.about, name='about'), #about page
    path('contact', views.contact, name='contact') #contact page
]
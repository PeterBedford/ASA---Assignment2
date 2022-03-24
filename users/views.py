from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import Registerform
from django.contrib import messages

class UserRegisterView(generic.CreateView):
    form_class = Registerform
    template_name = 'registration/register.html'
    success_url  = reverse_lazy('login')







'''def register(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return redirect('index')'''


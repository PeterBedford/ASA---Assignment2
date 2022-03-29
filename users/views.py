from re import template
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.models import Profile
from .forms import EditProfileForm, Registerform
from django.contrib import messages

@method_decorator(login_required, name='dispatch')
class UserRegisterView(generic.CreateView):
    form_class = Registerform
    template_name = 'registration/register.html'
    success_url  = reverse_lazy('login')

@method_decorator(login_required, name='dispatch')
class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/edit_profile_page.html'
    #fields = ['first_name', 'last_name', 'address', 'City', 'Country', 'Photo']
    success_url  = reverse_lazy('index')


@method_decorator(login_required, name='dispatch')
def profile(request):
    return render(request, 'profile.html')



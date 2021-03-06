from re import template
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from users.models import Profile
from .forms import EditProfileForm, PasswordChangeFormCustom, Registerform, ViewProfileForm, PasswordChangeFormCustom
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from . import views


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
class ViewProfilePage(generic.UpdateView):
    model = Profile
    form_class = ViewProfileForm
    template_name = 'registration/profile.html'
    #fields = ['first_name', 'last_name', 'address', 'City', 'Country', 'Photo']
    success_url  = reverse_lazy('index')


#password stuff

class PasswordsChangeView_(PasswordChangeView):
    form_class = PasswordChangeFormCustom
    #template_name = 'registration/change-password.html'
    success_url  = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})

'''@method_decorator(login_required, name='dispatch')
def profile(request):
    return render(request, 'profile.html')'''



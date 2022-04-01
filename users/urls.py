import imp
from re import template
from unicodedata import name
from django.urls import path, include
from . import views
from users.views import EditProfilePageView, PasswordsChangeView_, UserRegisterView, ViewProfilePage, PasswordsChangeView_

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('<int:pk>/profile/', ViewProfilePage.as_view(), name='view_profile_page'),
    # password
    path('password/', PasswordsChangeView_.as_view(template_name='registration/change-password.html'), name='change_password'),
    path('password_success', views.password_success, name="password_success")
]

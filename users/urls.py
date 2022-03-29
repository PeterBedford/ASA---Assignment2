import imp
from django.urls import path, include
from . import views
from users.views import EditProfilePageView, UserRegisterView, profile

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('profile', profile, name='profile'),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name='edit_profile_page')
]
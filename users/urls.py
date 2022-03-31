import imp
from django.urls import path, include
from . import views
from users.views import EditProfilePageView, UserRegisterView, ViewProfilePage

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('<int:pk>/profile/', ViewProfilePage.as_view(), name='view_profile_page')
]
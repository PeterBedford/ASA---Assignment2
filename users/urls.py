import imp
from django.urls import path, include
from . import views
from users.views import UserRegisterView, profile

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('profile', profile, name='profile'),
    #path('login', views.login, name='login'),
    #path('logout', views.logout, name='logout'),
    #path('<int:pk>/edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
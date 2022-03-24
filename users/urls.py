import imp
from django.urls import path, include
from .views import UserRegisterView


from users.views import UserRegisterView

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    #path('login', views.login, name='login'),
    #path('logout', views.logout, name='logout'),
    #path('<int:pk>/edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
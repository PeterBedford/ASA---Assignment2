
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')), #static pages urls
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('product/', include('product.urls')),
    path('admin/', admin.site.urls),
]

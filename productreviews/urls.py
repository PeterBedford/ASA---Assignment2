
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')), #static pages urls
    path('users/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('', include('product.urls')),
    path('admin/', admin.site.urls),
]

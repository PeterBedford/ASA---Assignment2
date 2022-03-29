
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')), #static pages urls
    path('users/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('', include('product.urls')),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

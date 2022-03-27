from django.urls import path, include
from product.views import ProductView


urlpatterns = [
   path('product/<int:pk>', ProductView.as_view(), name="product")
]
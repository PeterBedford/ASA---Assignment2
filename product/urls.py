from django.urls import path, include
from product.views import ProductView, AddReviewView, ReviewDelete, ReviewUpdate, ReviewDetail, allProducts


urlpatterns = [
   path('product/<int:pk>', ProductView.as_view(), name="product"),
   path('products', allProducts, name="products"),
   # review urls
   path('review/<int:pk>/remove', ReviewDelete.as_view(), name='deletereview'),
   path('product/<int:pk>/review/', AddReviewView.as_view(), name="add_review"),
   path('review/edit/<int:pk>', ReviewUpdate.as_view(), name="edit_review"),
   path('review/detail/<int:pk>', ReviewDetail.as_view(), name="detail_review")
]
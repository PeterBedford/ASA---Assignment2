from itertools import product
from pyexpat import model
from re import template
from statistics import mode
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from product.forms import CreateReviewForm, UpdateReviewForm
from product.models import Product, Review
from django.template.response import TemplateResponse

class ProductView(DetailView):
    model = Product
    template_name = 'products/product.html'

class AddReviewView(CreateView):
    model = Review
    form_class = CreateReviewForm
    template_name = 'products/add_review.html'

    '''def add_product_name_header(self):
        product_id = self.kwargs['pk']
        product = Product.objects.filter(id=product_id)
        return TemplateResponse()'''

    def form_valid(self, form):
        #getting current user id and assigning to Author
        form.instance.Author = self.request.user
        #getting product id from url and assigning to product in review model.
        form.instance.Product_id = self.kwargs['pk'] 
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product', kwargs={'pk': self.kwargs['pk']})
    
    
    
    
class ReviewDelete(DeleteView):
    model = Review
    #no custom form needed
    template_name = 'products/delete_review.html'
    
    def get_success_url(self):
        return reverse_lazy('index') # change at some point


class ReviewUpdate(UpdateView):
    model = Review
    form_class = UpdateReviewForm
    template_name = 'products/edit_review.html'

    def get_success_url(self):
        return reverse_lazy('index')






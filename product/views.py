from itertools import product
from pyexpat import model
from re import template
from statistics import mode
from urllib import request
from django import forms
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from product.forms import CreateReviewForm, DetailReviewForm, UpdateReviewForm
from product.models import Product, Review
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.models import Profile
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.core.paginator import Paginator

class ProductView(DetailView):
    model = Product
    template_name = 'products/product.html'
    fields = ['name', 'brand', 'average_cost', 'category', 'date_released', 'description', 'photo']


def allProducts(request):

    products = Product.objects.all()
    
    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products
    }

    return render(request, 'products/all_products.html', context)



@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class AddReviewView(CreateView):
    model = Review
    form_class = CreateReviewForm
    template_name = 'products/add_review.html'


    def form_valid(self, form):

        #check
        user_reviews = Review.objects.filter(Author = self.request.user).exists()

        if user_reviews == False:
            url_back = reverse_lazy('product', kwargs={'pk': self.kwargs['pk']})
            #messagev = messages.error(request, 'You have already posted a review for this product')
            return redirect(url_back)
        else:
            #getting current user id and assigning to Author
            form.instance.Author = self.request.user
            #getting product id from url and assigning to product in review model.
            form.instance.Product_id = self.kwargs['pk'] 
            return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product', kwargs={'pk': self.kwargs['pk']})
    
    
    
@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class ReviewDelete(DeleteView):
    model = Review
    #no custom form needed
    template_name = 'products/delete_review.html'

    #product.id = Review.objects.get(Product.id)
    
    def get_success_url(self):
        #return reverse_lazy('index') # change at some point
        #eview_id = self.kwargs['pk']
        #q = Review.objects.raw('''SELECT Product_id FROM product_review WHERE id = %s''', [review_id])
        #product_id = Review.objects.get(Product.id)
        #for i in product_id:
        #    i.id
       
        return reverse_lazy('index')



@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class ReviewUpdate(UpdateView):
    model = Review
    form_class = UpdateReviewForm
    template_name = 'products/edit_review.html'

    def get_success_url(self):
        return reverse_lazy('index')



@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class ReviewDetail(DetailView):
    model = Review
    template_name = 'products/detail_review.html'



    

    def get_success_url(self):
        return reverse_lazy('index')




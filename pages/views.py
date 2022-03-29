import re
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from pages.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

from product.views import ProductView
from productreviews.settings import EMAIL_HOST_USER

def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Product Reviews Website || Enquiry'
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message']
            }
            message = "\n".join(body.values())
            
            try:
                send_mail(
                    'Product Reviews || Enquiry Form Response',
                    message,
                    settings.EMAIL_HOST_USER,
                    ['b8017339@my.shu.ac.uk'],
                    fail_silently=False
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("index")

    form = ContactForm()
    return render(request, 'pages/contact.html', {'form':form})
   

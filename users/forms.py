from pyexpat import model
from tkinter import PhotoImage
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from users.models import Profile
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField

class Registerform(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta: 
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )

    def __init__(self, *args, **kwargs):
        super(Registerform, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class Profileform(forms.ModelForm):
   

    class Meta: 
        model = Profile
        fields = ('first_name', 'last_name', 'address', 'City', 'Country', 'Photo' )

    def __init__(self, *args, **kwargs):
        super(Profileform, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['City'].widget.attrs['class'] = 'form-control'
        self.fields['Country'].widget.attrs['class'] = 'form-control'
        self.fields['Photo'].widget.attrs['class'] = 'form-control'



class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        html =  Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))

class EditProfileForm(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ('first_name', 'last_name', 'address', 'City', 'Country', 'Photo' )

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['City'].widget.attrs['class'] = 'form-control'
        self.fields['Country'].widget.attrs['class'] = 'form-control'
        
        #self.fields['Photo'].widget.attrs['class'] = 'form-control'
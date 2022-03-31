from django import forms
from product.models import Review







class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'description')
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'description')
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class DetailReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('Product', 'rating', 'description')
        widgets = {
            
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        
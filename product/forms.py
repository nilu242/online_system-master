from django import forms

from .models import Product


class ProductUpdateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price']

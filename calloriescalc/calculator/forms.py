from django import forms
from .models import Product, Meal

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'calories']

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['user_id', 'date', 'product', 'quantity']

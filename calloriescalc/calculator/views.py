from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Meal
from .forms import ProductForm, MealForm

#There're adding, removing products and changing products

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'object': product})

def meal_list(request):
    meals = Meal.objects.all()
    return render(request, 'meal_list.html', {'meals': meals})

def meal_create(request):
    form = MealForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('meal_list')
    return render(request, 'meal_form.html', {'form': form})

def meal_edit(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    form = MealForm(request.POST or None, instance=meal)
    if form.is_valid():
        form.save()
        return redirect('meal_list')
    return render(request, 'meal_form.html', {'form': form})

def meal_delete(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        meal.delete()
        return redirect('meal_list')
    return render(request, 'meal_confirm_delete.html', {'object': meal})

from django.db import models

# Create your models here.

#Creating new models Product and Meal

class Product(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField()

class Meal(models.Model):
    user_id = models.IntegerField()
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
from django.db import models
from .product import Product
from django.contrib.auth.models import User

class MyWishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
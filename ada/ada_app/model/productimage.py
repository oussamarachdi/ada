from django.db import models
from .product import Product

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    File = models.CharField(max_length=100)

    def __str__(self):
        return self.name
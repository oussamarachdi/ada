from django.db import models
from .product import Product

class Region(models.Model):
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

from django.db import models
from .product import Product
from .myproduct import MyProduct

class SubCategory(models.Model):
    myproduct = models.ForeignKey(MyProduct, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name
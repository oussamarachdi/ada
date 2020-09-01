from django.db import models
from .subcategory import SubCategory
from .product import Product
from .myproduct import MyProduct



class Category(models.Model):
    myproduct = models.ForeignKey(MyProduct, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    isvisible = models.BooleanField(default=True)
    numberOfSearchRequests = models.IntegerField(default=0)

    def __str__(self):
        return self.name
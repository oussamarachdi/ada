from django.db import models
from django.conf import settings
from .product import Product


class MyWishList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

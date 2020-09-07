from django.db import models
from django.conf import settings
from .category import Category
from .subcategory import SubCategory
from .profile import Profile
from .product import Product
class MyProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    myproduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    isVisible = models.BooleanField(default=True)

    def __str__(self):
        return self.name
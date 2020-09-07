from django.db import models
from .category import Category
from .subcategory import SubCategory
from .profile import Profile
from .region import Region




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.FloatField(max_length=40)
    description = models.CharField(max_length=500)
    creationdate = models.DateTimeField(auto_now_add=True, blank=True)
    isFree = models.BooleanField(default=False)
    review = models.IntegerField()

    def __str__(self):
        return self.name
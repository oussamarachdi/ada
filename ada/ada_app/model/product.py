from django.db import models
from .productimage import ProductImage
from .profile import Profile
from .myproduct import MyProduct
from django.utils.timezone import timezone 

class Product(models.Model):
    myproduct = models.ForeignKey(MyProduct, on_delete=models.CASCADE)
    profiles = models.OneToOneField(Profile, on_delete=models.CASCADE)
    productimages = models.ForeignKey(ProductImage, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.FloatField(max_length=40)
    description = models.CharField(max_length=500)
    creationdate = models.DateTimeField(auto_now_add=True, blank=True)
    isFree = models.BooleanField(default=False)
    review = models.IntegerField()
    
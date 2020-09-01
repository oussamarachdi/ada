from django.conf import settings
from django.db  import models
from .product import Product
from .myproduct import MyProduct


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    myproduct = models.ForeignKey(MyProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    phoneisvisible = models.BooleanField(default=True)
    avatarS = models.CharField(max_length=100)
    avatarM = models.CharField(max_length=100)
    avatarL = models.CharField(max_length=100)
    language = models.CharField(max_length=40)
    gpsL = models.CharField(max_length=100)
    gpsA = models.CharField(max_length=100)

    def __str__(self):
        return self.name
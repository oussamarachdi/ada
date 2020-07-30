from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(max_length=40)
    description = models.CharField(max_length=500)
    creationdate = models.DateTimeField()
    isFree = models.BooleanField(default=False)
    review = models.IntegerField()

class ProductImage(models.Model):
    name = models.CharField(max_length=30)
    File = models.CharField(max_length=100)

class SubCategory(models.Model):
    name = models.CharField(max_length=20)

class Category(models.Model):
    name = models.CharField(max_length=20)


class MyWhishList(models.Model):
    pass

class Region(models.Model):
    name = models.CharField(max_length=15)

class Profile(models.Model):
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


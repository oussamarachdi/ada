from django.db import models

class ProductImage(models.Model):
    name = models.CharField(max_length=30)
    File = models.CharField(max_length=100)
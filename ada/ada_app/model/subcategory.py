from django.db import models
from .category import Category

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User

class MyProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    isVisible = models.BooleanField(default=True)

    def __str__(self):
        return self.name
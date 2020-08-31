from django.db import models
from django.conf import settings

class MyProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    isVisible = models.BooleanField(default=True)

    def __str__(self):
        return self.name
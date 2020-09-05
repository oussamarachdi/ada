from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    isvisible = models.BooleanField(default=True)
    numberOfSearchRequests = models.IntegerField(default=0)

    def __str__(self):
        return self.name
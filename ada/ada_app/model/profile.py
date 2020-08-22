from django.db  import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
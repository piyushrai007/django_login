from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return self.user.username

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

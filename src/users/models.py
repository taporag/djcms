from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(blank=True)
    phone = models.CharField(blank=True, max_length=15)
    locale = models.CharField(default='en', max_length=2)

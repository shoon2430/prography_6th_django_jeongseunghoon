from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    AUTH_USER = "user"
    AUTH_MANAGER = "manager"
    AUTH_CHOICES = [
        (AUTH_USER, "User"),
        (AUTH_MANAGER, "Manager")
    ]

    authority = models.CharField(
        choices=AUTH_CHOICES, max_length=8, default=AUTH_USER)

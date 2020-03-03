from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class User(AbstractUser):

    AUTH_USER = "user"
    AUTH_MANAGER = "manager"
    AUTH_CHOICES = [(AUTH_USER, "User"), (AUTH_MANAGER, "Manager")]

    authority = models.CharField(choices=AUTH_CHOICES, max_length=8, default=AUTH_USER)


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser): # MODEL IS NOT USED YET
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        verbose_name='User email'
    )
    
    username = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False,
        verbose_name='User user name'
    )
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']
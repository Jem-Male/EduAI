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
    
    LIMIT_CHOICES = [(i, str(i)) for i in range(0, 101)]
    
    ai_limit = models.IntegerField(
        choices=LIMIT_CHOICES,
        default=3
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
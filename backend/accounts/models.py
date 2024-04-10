from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=40, unique=False)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=88)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
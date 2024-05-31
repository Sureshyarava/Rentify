from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # groups = models.ManyToManyField(Group, related_name='customuser_groups')
    # user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=75)
    phone_number = models.CharField(max_length=12)

from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from core.models import BaseModel


# Create your models here.

class User(AbstractUser, BaseModel):
    name = models.CharField(verbose_name='Name', max_length=160)
    phone = models.IntegerField(null=True)
    address = models.TextField()
    picture = models.ImageField(verbose_name="Picture of User", width_field=40, height_field=50)

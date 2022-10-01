from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    package = models.CharField(max_length=32)
    price = models.IntegerField()
    size = models.CharField(max_length=32)
    picture = models.ImageField(verbose_name="Picture of Product")
    country = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)

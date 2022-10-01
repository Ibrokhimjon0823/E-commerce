# from django.db import models
#
# from django.contrib.auth.models import AbstractUser, PermissionsMixin
#
#
# # Create your models here.
#
# class Category(models.Model):
#     name = models.CharField(max_length=64)
#     description = models.TextField(blank=True)
#




#
# class OrderProduct(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.PROTECT)
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
#     price = models.DecimalField()
#     count = models.IntegerField()
#
#
# products = [
#     dict(
#         product=1,
#         count=3
#     ),
#     dict(
#         product=2,
#         count=3
#
#     )
# ]

from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin


# Create your models here.

class User(AbstractUser):
    phone = models.IntegerField()
    address = models.TextField()
    picture = models.ImageField(verbose_name="Picture of User", width_field=40, height_field=50)


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)


class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    package = models.CharField(max_length=32)
    price = models.IntegerField()
    size = models.CharField(max_length=32)
    picture = models.ImageField(verbose_name="Picture of Product")
    country = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)


class Payment(models.Model):
    class Type(models.TextChoices):
        CARD = "card", "Card"
        CASH = 'cash', "Cash"
    payment_type = models.CharField("Type", max_length=20, choices=Type.choices)


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    class Paid(models.TextChoices):
        PAID = "paid", "Paid"
        UNPAID = "unpaid", "Unpaid"

    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.OneToOneField(Product, on_delete=models.PROTECT)
    order_number = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.DecimalField()
    total = models.DecimalField()
    ship_date = models.DateTimeField()
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT)
    order_date = models.DateTimeField()
    status = models.CharField("Status", max_length=20, choices=Status.choices, default=Status.PENDING)
    paid = models.CharField("Paid", max_length=20, choices=Paid.choices, default=Paid.UNPAID)
    payment_date = models.DateTimeField()

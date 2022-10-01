from django.db import models

from products.models import Product
from users.models import User
from payments.models import Payment


# Create your models here.

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Completed"
        REJECTED = "rejected", "Rejected"

    class Paid(models.TextChoices):
        PAID = "paid", "Paid"
        UNPAID = "unpaid", "Unpaid"

    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.OneToOneField(Product, on_delete=models.PROTECT)
    order_number = models.IntegerField()
    price = models.IntegerField()
    discount = models.DecimalField("Discount", max_digits=5, decimal_places=2)
    ship_date = models.DateTimeField()
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT)
    order_date = models.DateTimeField()
    status = models.CharField("Status", max_length=20, choices=Status.choices, default=Status.PENDING)
    paid = models.CharField("Paid", max_length=20, choices=Paid.choices, default=Paid.UNPAID)
    payment_date = models.DateTimeField()


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total = models.DecimalField("Total", max_digits=10, decimal_places=2)


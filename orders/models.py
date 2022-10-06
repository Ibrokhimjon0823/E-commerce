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
    status = models.CharField("Status", max_length=20, choices=Status.choices, default=Status.PENDING)
    paid = models.CharField("Paid", max_length=20, choices=Paid.choices, default=Paid.UNPAID)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='order_details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    # def __str__(self):
    #     self.product

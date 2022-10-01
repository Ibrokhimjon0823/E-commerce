from django.db import models


# Create your models here.
class Payment(models.Model):
    class Type(models.TextChoices):
        CARD = "card", "Card"
        CASH = 'cash', "Cash"

    payment_type = models.CharField("Type", max_length=20, choices=Type.choices)

# Generated by Django 4.1.1 on 2022-10-06 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='total',
        ),
    ]

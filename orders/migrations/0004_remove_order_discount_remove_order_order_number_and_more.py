# Generated by Django 4.1.1 on 2022-10-06 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_quantity_alter_orderdetails_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ship_date',
        ),
    ]

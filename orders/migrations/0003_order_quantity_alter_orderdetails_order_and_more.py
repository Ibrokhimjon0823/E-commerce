# Generated by Django 4.1.1 on 2022-10-05 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_details', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
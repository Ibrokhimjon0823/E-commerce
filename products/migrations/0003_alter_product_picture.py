# Generated by Django 4.1.1 on 2022-10-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Picture of Product'),
        ),
    ]
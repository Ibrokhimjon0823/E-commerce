# Generated by Django 4.1.1 on 2022-10-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_created_at_user_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=160, verbose_name='Name'),
            preserve_default=False,
        ),
    ]

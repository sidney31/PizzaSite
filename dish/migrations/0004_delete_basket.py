# Generated by Django 5.0.1 on 2024-01-11 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0003_basket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Basket',
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-12 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_basket_total_price_alter_dishinbasket_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='count',
        ),
    ]

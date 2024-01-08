# Generated by Django 5.0.1 on 2024-01-08 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_rename_navitem_header_alter_header_options_and_more'),
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='header',
            options={'verbose_name': 'Элемент хеадера', 'verbose_name_plural': 'Элементы хеадера'},
        ),
        migrations.RemoveField(
            model_name='header',
            name='nav_item',
        ),
        migrations.AddField(
            model_name='header',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='header',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-11 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='skill',
            new_name='sku',
        ),
    ]

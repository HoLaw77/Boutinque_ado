# Generated by Django 4.2.7 on 2023-11-11 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_categories_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

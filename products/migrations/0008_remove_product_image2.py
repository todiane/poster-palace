# Generated by Django 3.2.23 on 2023-12-14 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_image2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
    ]
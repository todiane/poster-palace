# Generated by Django 3.2.23 on 2023-12-14 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20231127_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
    ]
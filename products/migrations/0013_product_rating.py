# Generated by Django 3.2.23 on 2023-12-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_delete_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]

# Generated by Django 3.2.23 on 2024-01-03 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]

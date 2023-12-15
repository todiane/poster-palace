# Generated by Django 3.2.23 on 2023-12-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_image2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('L', 'Large'), ('XL', 'Extra Large')], max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.AddField(
            model_name='product',
            name='sizes_available',
            field=models.ManyToManyField(related_name='products', to='products.Size'),
        ),
    ]
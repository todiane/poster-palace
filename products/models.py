from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True, null=True, blank=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        ordering = ['name']
 
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Size(models.Model):
    name = models.CharField(max_length=15)
    code = models.CharField(max_length=15)
    price = models.DecimalField(default=9.95, 
                                max_digits=10, decimal_places=2)


class Product(models.Model):
    sku = models.CharField(max_length=15, 
                           default=get_random_string, 
                           null=True, blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)  
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)
    sizes = models.ManyToManyField(Size)
    category = models.ForeignKey('Category', null=True, 
                                 blank=True, on_delete=models.SET_NULL)
    available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, 
                                 null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

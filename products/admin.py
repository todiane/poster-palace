from django.contrib import admin
from .models import Product, Category

        
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'sizes',
                    'available', 'category', 'created']
    list_filter = ['available', 'category', 'created',]
    list_editable = ['price', 'available', 'sizes',]
    prepopulated_fields = {'slug': ('name',)}
from django.contrib import admin
from .models import Product, Category, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'sizes',
                    'available', 'category', 'rating', 'created']
    list_filter = ['available', 'category', 'created',]
    list_editable = ['price', 'available', 'sizes', 'category', 'rating',]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Reviews)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at',]
    list_filter = ['product', 'user', 'created_at',]
    list_editable = ['rating']
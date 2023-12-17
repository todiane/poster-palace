from django.contrib import admin
from .models import Product, Category, Review

        
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'sizes',
                    'available', 'category', 'created']
    list_filter = ['available', 'category', 'created',]
    list_editable = ['price', 'available', 'sizes', 'category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating','comment', 'created_at']
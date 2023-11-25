from django.contrib import admin
from .models import Product, Category, Size

        
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'price']
    list_editable = ['code', 'price']


@admin.register(Product)  
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('sizes',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "sizes":
             kwargs["queryset"] = Size.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    prepopulated_fields = {'slug': ('name',)}

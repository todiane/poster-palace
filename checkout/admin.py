from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'created', 'updated',
                       'delivery_cost', 'order_total',
                       'grand_total',
                       )

    fields = ('order_number', 'created', 'updated', 'first_name', 'last_name',
              'email', 'phone_number', 'street_address1', 
              'street_address2',  'town_or_city', 
              'county', 'postcode', 'country',  
              'delivery_cost', 'order_total', 'grand_total',
              )

    list_display = ('order_number', 'created', 'first_name', 'last_name',
                    'order_total', 'delivery_cost',
                    'grand_total', 'updated',)

    ordering = ('-created',)


admin.site.register(Order, OrderAdmin)
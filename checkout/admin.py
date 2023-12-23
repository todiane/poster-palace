from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'created', 'updated',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_pid',
                       )

    fields = ('order_number', 'created', 'updated', 'full_name',
              'email', 'phone_number', 'street_address1',
              'street_address2',  'town_or_city',
              'county', 'postcode', 'country',
              'delivery_cost', 'order_total', 'grand_total', 'original_bag',
              'stripe_pid',
              )

    list_display = ('order_number', 'created', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total', 'updated',)

    ordering = ('-created',)


admin.site.register(Order, OrderAdmin)

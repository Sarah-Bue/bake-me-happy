from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    This class is used to display the order line items in the admin panel.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    This class is used to display the orders in the admin panel.
    """

    inlines = (OrderLineItemAdminInline,)

    # Readonly / non-editable fields
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_basket',
                       'stripe_pid')

    # Fields to be displayed in the admin panel
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_basket',
              'stripe_pid')

    # Fields to be displayed in the list view
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # Order by date, most recent first
    ordering = ('-date',)


# Register the models
admin.site.register(Order, OrderAdmin)

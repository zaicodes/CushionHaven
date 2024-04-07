from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineItemAdminInline]

    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total', 'grand_total')

    fieldsets = (
        (None, {
            'fields': ('order_number', 'date', 'full_name', 'email', 'phone_number')
        }),
        ('Delivery Address', {
            'fields': ('country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county')
        }),
        ('Order Summary', {
            'fields': ('delivery_cost', 'order_total', 'grand_total'),
            'classes': ('collapse',)
        }),
    )

    list_display = ('order_number', 'date', 'full_name', 'order_total', 'delivery_cost', 'grand_total')
    list_filter = ('date',)
    search_fields = ('order_number', 'full_name')
    ordering = ('-date',)

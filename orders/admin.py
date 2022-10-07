from django.contrib import admin
from .models import Order, OrderDetails
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = (
        'customer', 'status', 'paid',
    )
    list_filter = (
        'customer', 'status', 'paid',
    )
    search_fields = ('customer', )


class OrderDetailsAdmin(admin.ModelAdmin):
    model = OrderDetails
    list_display = (
        'order', 'product', 'price', 'quantity'
    )
    list_filter = (
        'product', 'price', 'quantity',
    )
    search_fields = ('product', )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)

from django.contrib import admin
from .models import Product
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = (
        'name', 'category', 'price', 'country',
    )
    list_filter = (
        'name', 'category', 'country',
    )
    search_fields = ('name', 'category')


admin.site.register(Product, ProductAdmin)

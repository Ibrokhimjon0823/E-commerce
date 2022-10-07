from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        'id', 'username', 'phone', 'is_staff', 'is_active',
    )
    list_filter = (
        'is_staff', 'is_active', 'phone',
    )
    readonly_fields = ('created_at', 'updated_at', 'last_login')
    search_fields = ('email', 'name')
    ordering = ('created_at',)


admin.site.register(User, CustomUserAdmin)

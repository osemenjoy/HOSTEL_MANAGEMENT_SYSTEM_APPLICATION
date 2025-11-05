from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ['matric_number']
    list_display = ['matric_number', 'first_name', 'last_name', 'is_staff']
    fieldsets = (
        (None, {'fields': ('matric_number', 'password')}),
        ('Personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('matric_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('matric_number',)

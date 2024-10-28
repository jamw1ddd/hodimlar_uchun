from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Set only existing fields for 'list_display'
    list_display = ('username', 'phone_number')  # Adjust to match your model fields

    # Set fieldsets to use only fields present in CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Set add_fieldsets for the user creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone_number', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

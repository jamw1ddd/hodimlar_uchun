from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'is_staff')  # Use only the fields defined in CustomUser
    search_fields = ('username', 'phone_number')  # Add any other fields you want to search by

admin.site.register(CustomUser, CustomUserAdmin)

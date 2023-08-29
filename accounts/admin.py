from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserCreate(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'is_superuser', 'is_staff', 'is_active']

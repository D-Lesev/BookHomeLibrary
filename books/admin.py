from django.contrib import admin
from .models import NewBookCreation


@admin.register(NewBookCreation)
class BookCreationAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "genre"]


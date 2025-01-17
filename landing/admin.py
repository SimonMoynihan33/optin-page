from django.contrib import admin
from .models import OptIn

@admin.register(OptIn)
class OptInAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'email')  # Fields to show in the admin list view
    search_fields = ('nickname', 'email')  # Add search functionality
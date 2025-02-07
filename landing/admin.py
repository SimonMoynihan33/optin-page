from django.contrib import admin
from .models import OptIn


@admin.register(OptIn)
class OptInAdmin(admin.ModelAdmin):
    list_display = ("nickname", "email")
    search_fields = ("nickname", "email")

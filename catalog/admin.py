from django.contrib import admin
from catalog.models import DishType


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ["name", ]

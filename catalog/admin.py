from django.contrib import admin
from catalog.models import DishType, Ingredient


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ["name", ]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ["name", ]

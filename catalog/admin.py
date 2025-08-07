from django.contrib import admin
from catalog.models import DishType, Ingredient, Dish


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ["name", ]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ["name", ]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ["name", ]
    list_display = ["name", "price", "dish_type", ]
    list_filter = ["dish_type", ]
    filter_horizontal = ["cooks", "ingredients", ]

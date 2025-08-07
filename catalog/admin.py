from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import DishType, Ingredient, Dish, Cook


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


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience", )}), )
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )

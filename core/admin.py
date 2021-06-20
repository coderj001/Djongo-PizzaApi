from django.contrib import admin
from core.models import (
    PizzaSize,
    PizzaTopping,
    Pizza
)


@admin.register(PizzaSize)
class PizzaSizeAdmin(admin.ModelAdmin):
    pass


@admin.register(PizzaTopping)
class PizzaToppingAdmin(admin.ModelAdmin):
    pass


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type_pizza',
        'size_pizza',
        'topping_pizza'
    )

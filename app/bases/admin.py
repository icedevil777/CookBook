from django.contrib import admin
from .models import Ingredient
from .models import Recipes


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name']

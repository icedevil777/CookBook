from django.contrib import admin

from .models import Recipes

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

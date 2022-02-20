from django.db import models


class Recipes(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField('Ingredient', blank=False)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

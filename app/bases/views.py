from django.shortcuts import render

from .models import Recipes


def home(request):
    recipes = Recipes.objects.all()
    return render(request, 'home.html', {
        'recipes': recipes,
    })


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')

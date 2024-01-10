from django.shortcuts import render, get_object_or_404
from .models import Dish


def index(request):
    pass


def get_dish_info(request, dish_slug):
    dishes = get_object_or_404(Dish, slug=dish_slug)
    context = {
        'dishes': dishes,
    }
    return render(request, 'dish/dish_page.html', context)

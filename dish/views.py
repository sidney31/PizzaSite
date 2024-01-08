from django.shortcuts import render, get_object_or_404
from .models import Pizza


def index(request):
    pass


def get_dish_info(request, dish_slug):
    pizza = get_object_or_404(Pizza, slug=dish_slug)
    context = {
        'pizza': pizza,
    }
    return render(request, 'dish/dish_page.html', context)

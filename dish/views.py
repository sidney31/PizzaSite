from django.shortcuts import render, get_object_or_404
from .models import Dish
from order.models import Basket


def index(request):
    pass


def get_dish_info(request, dish_slug):
    dishes = get_object_or_404(Dish, slug=dish_slug)
    basket = Basket.objects.get(id=1)
    context = {
        'dishes': dishes,
        'basket': basket,
    }
    return render(request, 'dish/dish_page.html', context)

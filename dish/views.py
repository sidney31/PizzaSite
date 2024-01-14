from django.shortcuts import render, get_object_or_404
from .models import Dish
from cart.cart import Cart


def index(request):
    pass


def get_dish_info(request, dish_slug):
    dish = get_object_or_404(Dish, slug=dish_slug)
    cart = Cart(request)
    context = {
        'dish': dish,
        'cart': cart,
    }
    return render(request, 'dish/dish_page.html', context)

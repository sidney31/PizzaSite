from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from dish.models import Dish


def cart_add(request, dish_id):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    cart.add(dish)

    return JsonResponse({'cart': cart.cart})


def cart_remove(request, dish_id, quantity=0):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    cart.remove(dish, quantity)

    return JsonResponse({'cart': cart})


def index(request):
    cart = Cart(request)
    return render(
        request,
        'cart/cart_page.html',
        {'cart': cart}
    )

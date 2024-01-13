from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from dish.models import Dish


def cart_add(request, dish_id):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    if dish_id in cart.cart:
        cart.add(dish_id, 1)
    else:
        cart.add(dish)

    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, dish_id, quantity=0):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    cart.remove(dish, quantity)

    return redirect(request.META.get('HTTP_REFERER'))


def index(request):
    cart = Cart(request)
    return render(
        request,
        'cart/cart_page.html',
        {'cart': cart}
    )

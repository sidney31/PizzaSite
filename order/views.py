from django.shortcuts import render, redirect
from .models import Basket, DishInBasket


def index(request):
    if not Basket.objects.get(id=1):
        Basket.objects.create()

    context = {
        'basket': Basket.objects.get(id=1),
        'DishesInBasket': DishInBasket.objects.all(),
    }
    return render(request, 'order/order_page.html', context)


def add_dish_to_basket(request, dish_id):
    basket = Basket.objects.get(id=1)
    dish_in_basket = DishInBasket.objects.filter(dish_id=dish_id).first()
    if dish_in_basket:
        dish_in_basket.quantity += 1
        dish_in_basket.save()
    else:
        dish_in_basket = DishInBasket.objects.create(dish_id=dish_id)

    basket.total_price += dish_in_basket.dish.price
    basket.save()

    return redirect(request.META.get('HTTP_REFERER'))


def remove_dish_from_basket(request, dish_id):
    basket = Basket.objects.get(id=1)
    dish_in_basket = DishInBasket.objects.filter(dish_id=dish_id).first()

    basket.total_price -= dish_in_basket.dish.price
    basket.save()

    if dish_in_basket.quantity == 1:
        basket.total_price -= dish_in_basket.dish.price * dish_in_basket.quantity
        dish_in_basket.delete()
    else:
        basket.total_price -= dish_in_basket.dish.price
        dish_in_basket.quantity -= 1
        dish_in_basket.save()

    return redirect(request.META.get('HTTP_REFERER'))


def full_remove_dish_from_basket(request, dish_id):
    basket = Basket.objects.get(id=1)
    dish_in_basket = DishInBasket.objects.filter(dish_id=dish_id).first()

    basket.total_price -= dish_in_basket.dish.price * dish_in_basket.quantity
    dish_in_basket.delete()

    return redirect(request.META.get('HTTP_REFERER'))

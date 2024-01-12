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
    dish_in_basket = DishInBasket.objects.create(dish_id=dish_id)
    old_total_price = Basket.objects.get(id=1).total_price

    basket.total_price = old_total_price + dish_in_basket.dish.price
    basket.save()

    return redirect('menu')


def remove_dish_from_basket(request, dish_id):
    basket = Basket.objects.get(id=1)
    dish_in_basket = DishInBasket.objects.filter(dish_id=dish_id).first()
    old_total_price = Basket.objects.get(id=1).total_price

    basket.total_price = old_total_price - dish_in_basket.dish.price
    basket.save()

    dish_in_basket.delete()

    return redirect('order:index')

from django.shortcuts import render
from dish.models import Category
from .models import ItemOfHeader
from order.models import Basket, DishInBasket


def index(request):
    context = {
        'categories': Category.objects.all(),
        'header': ItemOfHeader.objects.all(),
        'basket': Basket.objects.get(id=1),
        'dishesInBasket': DishInBasket.objects.all(),
    }
    return render(request, 'menu/menu_page.html', context)


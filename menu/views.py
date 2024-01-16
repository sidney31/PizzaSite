from django.shortcuts import render
from dish.models import Category
from .models import ItemOfHeader
from cart.cart import Cart


def index(request):
    print(Cart(request).get_total_price())
    context = {
        'categories': Category.objects.all(),
        'header': ItemOfHeader.objects.all(),
        'cart': Cart(request),
    }
    return render(request, 'menu/menu_page.html', context)


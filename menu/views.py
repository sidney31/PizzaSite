from django.shortcuts import render
from dish.models import Category
from .models import ItemOfHeader
from order.models import Basket


def index(request):
    context = {
        'categories': Category.objects.all(),
        'header': ItemOfHeader.objects.all(),
        'basket': Basket.objects.get(id=1),
    }
    return render(request, 'menu/menu_page.html', context)


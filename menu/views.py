from django.shortcuts import render
from dish.models import Category
from .models import ItemOfHeader


def index(request):
    context = {
        'categories': Category.objects.all(),
        'header': ItemOfHeader.objects.all(),
    }
    return render(request, 'menu/menu_page.html', context)


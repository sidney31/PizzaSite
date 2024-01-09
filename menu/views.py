from django.shortcuts import render
from dish.models import Pizza
from .models import ItemOfHeader


def index(request):
    context = {'dishes': Pizza.objects.all(),
               'header': ItemOfHeader.objects.all()}
    return render(request, 'menu/menu_page.html', context)
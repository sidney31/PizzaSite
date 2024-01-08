from django.shortcuts import render
from dish.models import Pizza
from .models import Header


def index(request):
    context = {'dishes': Pizza.objects.all(),
               'header': Header.objects.all()}
    return render(request, 'menu/menu_page.html', context)

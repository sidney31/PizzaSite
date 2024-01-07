from django.shortcuts import render
from dish.models import Pizza


def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'home/home_page.html', context={'pizzas': pizzas})

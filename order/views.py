from django.shortcuts import render


def index(request):
    return render(request, 'order/order_page.html')

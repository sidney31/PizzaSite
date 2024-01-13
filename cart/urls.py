from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:dish_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:dish_id>/<int:quantity>', views.cart_remove, name='cart_remove'),
]

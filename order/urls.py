from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:dish_id>/', views.add_dish_to_basket, name='add_dish_to_basket'),
    path('remove/<int:dish_id>', views.remove_dish_from_basket, name='remove_dish_from_basket'),
    path('full_remove/<int:dish_id>', views.full_remove_dish_from_basket, name='full_remove_dish_from_basket'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='dishes'),
    path("<slug:dish_slug>/", views.get_dish_info, name='dish'),
]

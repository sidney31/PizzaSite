from django.urls import path
from . import views

urlpatterns = [
    path("<slug:dish_slug>/", views.get_dish_info, name='dish'),
]

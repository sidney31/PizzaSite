from django.db import models
from dish.models import Dish


class DishInBasket(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)


class Basket(models.Model):
    dishes = models.ForeignKey(DishInBasket, on_delete=models.CASCADE, null=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

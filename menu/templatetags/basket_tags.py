from django import template
from order.models import DishInBasket
from dish.models import Dish

register = template.Library()


@register.simple_tag(takes_context=True)
def get_quantity_tag(context, dish_id):
    dish = Dish.objects.get(id=dish_id)
    dish_in_basket = DishInBasket.objects.filter(dish=dish).first()
    quantity = dish_in_basket.quantity if dish_in_basket else None

    return {
        'request': context['request'],
        'quantity': quantity,
    }

from django import template
from cart.cart import Cart

register = template.Library()


@register.simple_tag(takes_context=True)
def get_quantity(context, dish_id):
    cart = Cart(context['request'])
    quantity = cart.get_quantity(dish_id)
    return {
        'request': context['request'],
        'quantity': quantity,
    }

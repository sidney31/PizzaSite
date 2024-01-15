from decimal import Decimal

from django.conf import settings
from dish.models import Dish


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, dish, quantity=1):
        dish_id = str(dish.id)
        if dish_id not in self.cart:
            self.cart[dish_id] = {
                'quantity': 0,
                'price': str(dish.price)
            }

        self.cart[dish_id]['quantity'] += quantity

        self.save()

    def remove(self, dish, quantity=0):
        dish_id = str(dish.id)
        if quantity == 0 or self.cart[dish_id]['quantity'] == 1:
            del self.cart[dish_id]
        else:
            self.cart[dish_id]['quantity'] -= 1

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def __iter__(self):
        dishes_ids = self.cart.keys()

        dishes = Dish.objects.filter(id__in=dishes_ids)
        for dish in dishes:
            self.cart[str(dish.id)]['dish'] = dish

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    @property
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity']
                   for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_quantity(self, dish_id):
        if str(dish_id) in self.cart:
            return self.cart[str(dish_id)]['quantity']

        return 0

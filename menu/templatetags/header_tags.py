from django import template
from dish.models import Category
from menu.models import ItemOfHeader

register = template.Library()


@register.inclusion_tag('tags/header.html', takes_context=True)
def header_tag(context):
    context['categories'] = Category.objects.all()
    context['headerItems'] = ItemOfHeader.objects.all()
    return context

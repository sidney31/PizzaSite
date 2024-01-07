from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


class PizzaPage(Page):
    pass


@register_snippet
class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('size'),
        FieldPanel('price'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

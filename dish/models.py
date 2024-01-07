from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

from transliterate import translit, get_available_language_codes


class PizzaPage(Page):
    pass


@register_snippet
class Pizza(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
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

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.name, 'ru', reversed=True))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('dish', kwargs={'dish_slug': self.slug})

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

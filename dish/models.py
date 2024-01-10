from django.db import models

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.snippets.models import register_snippet

from transliterate import translit


class DishPage(Page):
    pass


@register_snippet
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


@register_snippet
class Dish(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='+', null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.CharField(max_length=255)
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
        FieldPanel('category'),
        FieldPanel('description'),
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
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        
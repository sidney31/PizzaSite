from django.db import models

from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


class MenuPage(Page):
    pass


@register_snippet
class Header(models.Model):
    title = models.CharField(max_length=20, default='')
    page = models.ForeignKey('wagtailcore.Page', blank=True, null=True, on_delete=models.SET_NULL)
    
    panels = [
        FieldPanel('title'),
        PageChooserPanel('page'),
    ]
    
    # type = forms.ChoiceField(required=True, choices=[
    #     ('link', 'Link'),
    #     ('dropdown', 'Dropdown'),
    # ], default='link')
    
    class Meta:
        verbose_name = 'Элемент хеадера'
        verbose_name_plural = 'Элементы хеадера'
        
    def __str__(self):
        return self.title

    
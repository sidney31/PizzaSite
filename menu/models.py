from django import forms
from django.db import models

from wagtail.admin.panels import (FieldPanel, 
                                  PageChooserPanel, 
                                  InlinePanel,
                                  MultiFieldPanel,
                                  HelpPanel)
from wagtail.models import Page, Orderable
from wagtail.snippets.models import register_snippet

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

class MenuPage(Page):
    pass


class LinkTextMixin(models.Model):
    title = models.CharField(max_length=20,
                             blank=False, 
                             null=True)
    page = models.ForeignKey('wagtailcore.Page',
                             blank=True,
                             null=True,
                             on_delete=models.SET_NULL,
                             related_name='+')

    panels = [
        FieldPanel('title'),
        PageChooserPanel('page'),
    ]

    def __str__(self):
        return self.title


@register_snippet
class ItemOfHeader(LinkTextMixin, ClusterableModel):

    class TypeChoice(models.TextChoices):
        LINK = 'L', 'Link'
        DROPDOWN = 'D', 'Dropdown'
        
    type = models.TextField(max_length=1, 
                            choices=TypeChoice.choices, 
                            default=TypeChoice.LINK)

    panels = [
        LinkTextMixin.panels[0],
        FieldPanel('type', widget=forms.Select),
        LinkTextMixin.panels[1],
        MultiFieldPanel([
            InlinePanel('drop_down_item'),
        ], heading = 'Items'),
    ]

    class Meta:
        verbose_name = 'Элемент хеадера'
        verbose_name_plural = 'Элементы хеадера'
     
        
class ItemOfDropDown(LinkTextMixin, Orderable):
    parent_item = ParentalKey(
        ItemOfHeader, 
        on_delete=models.CASCADE,
        related_name='drop_down_item',
    )
    
    panels = LinkTextMixin.panels
    
    def __str__(self):
        return LinkTextMixin.title
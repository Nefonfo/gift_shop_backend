from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class GenericPage(Page):
    header_text = models.CharField(null = True, blank = False, max_length=60, verbose_name = _('Header Text'))
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name = _('Header Image')
    )
    body = RichTextField(null = True, blank = False, verbose_name = _('Body'))

    content_panels = Page.content_panels + [
        FieldPanel('header_text'),
        ImageChooserPanel('header_image'),
        FieldPanel('body')
    ]
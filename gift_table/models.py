from django.db import models

from modelcluster.models import ClusterableModel
from modelcluster.models import ParentalKey

from django.utils.translation import ugettext_lazy as _

from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel

from registration.models import User

# Create your models here.

@register_snippet
class GiftTable(ClusterableModel, models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Client'), default=None, null = True, blank = True)
    
    panels = [
        SnippetChooserPanel('client'),
        InlinePanel('product_gift_table', label = 'products'),
    ]
    

@register_snippet
class ProductGiftTable(models.Model):
    gift_table = ParentalKey('gift_table.GiftTable', on_delete = models.CASCADE, related_name = 'product_gift_table')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='gift_table_product')
    
    panels = [
        SnippetChooserPanel('product'),
    ]
    
    class Meta:
        unique_together = ('gift_table', 'product')
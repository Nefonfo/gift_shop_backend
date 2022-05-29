from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.models import ClusterableModel

from taggit.models import TaggedItemBase
from autoslug import AutoSlugField

from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel
)

# Create your models here.
""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This is will create a relation of tags for products, this will be the    │
  │ relation of many to many (between product and taggit                     │
  │ models)                                                                  │
  └──────────────────────────────────────────────────────────────────────────┘
 """
@register_snippet
class ProductTag(TaggedItemBase):
    content_object = ParentalKey(
        'product.Product',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This will be a model to create a one to many relationship but with the   │
  │ feature to be ordered (will create a list of this many objects and be    │
  │ ordered as we                                                            │
  │ need)                                                                    │
  └──────────────────────────────────────────────────────────────────────────┘
 """
@register_snippet
class ProductCarouselImages(Orderable):
    product = ParentalKey('product.Product', related_name = 'product_images')
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    panels = [ImageChooserPanel("carousel_image")]
    
""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This will be our product model for the database, will be related with a  │
  │ lot of tables and                                                        │
  │ models                                                                   │
  └──────────────────────────────────────────────────────────────────────────┘
 """
@register_snippet
class Product(ClusterableModel, models.Model):
    name = models.CharField(max_length=70, verbose_name=_('Name'))
    url = AutoSlugField(populate_from='name', unique = True)
    description = RichTextField(verbose_name=_('Description'))
    price = models.FloatField(verbose_name=_('Price'))
    stock = models.IntegerField(verbose_name=_('Stock'))
    available = models.BooleanField(verbose_name=_('Available'))
    tags = ClusterTaggableManager(through=ProductTag, blank=True, verbose_name=_('Categories'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('price'),
        FieldPanel('stock'),
        FieldPanel('available'),
        MultiFieldPanel(
            [InlinePanel("product_images", max_num=5, min_num=1, label="Image")],
            heading="Carousel Images",
        ),
        FieldPanel("tags"),
    ]
    
    def __str__(self) -> str:
        return self.name
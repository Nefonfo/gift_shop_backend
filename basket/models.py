from django.db import models

from modelcluster.models import ClusterableModel
from modelcluster.models import ParentalKey

from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel

from registration.models import User

# Create your models here.
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This model create a db table for discounts code                          │
  └──────────────────────────────────────────────────────────────────────────┘
 """
@register_snippet
class DiscountCode(models.Model):
    name = models.CharField(max_length=10, verbose_name=_('Name'))
    code = models.CharField(max_length=10, verbose_name=_('Code'), unique=True)
    percentage = models.DecimalField(max_digits=3, decimal_places=0, validators=PERCENTAGE_VALIDATOR)
    mount = models.FloatField(verbose_name=_('Mount'))
    
    panels = [
        FieldPanel('name'),
        FieldPanel('code'),
        FieldPanel('percentage'),
        FieldPanel('mount')
    ]
    
    
""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This model create a db table for gift code                               │
  └──────────────────────────────────────────────────────────────────────────┘
 """
@register_snippet
class GiftCode(models.Model):
    basket = models.OneToOneField('basket.Basket', on_delete=models.CASCADE)
    code = models.CharField(max_length=10, verbose_name=_('Code'), unique=True)
    mount = models.FloatField(verbose_name=_('Mount'))
    
    panels = [
        FieldPanel('code'),
        FieldPanel('mount')
    ]


""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This model create a basket table, this will be connected with an unique  │
  │ user. Its important to consider that the model with be related with the  │
  │ product model but with a many to many                                    │
  │ relationship                                                             │
  └──────────────────────────────────────────────────────────────────────────┘
 """
@register_snippet
class Basket(ClusterableModel, models.Model):
    client = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name=_('Client'))
    discount = models.ForeignKey('basket.DiscountCode', on_delete=models.SET_NULL, null = True, blank = True, verbose_name=_('Discount'))
    
    panels = [
        SnippetChooserPanel('client'),
        InlinePanel('product_basket', label = 'products'),
        SnippetChooserPanel('discount')
    ]
    
    def quantity(self) -> int:
        products_quantity = 0
        for product in self.client.basket.product_basket.all():
            products_quantity = int(products_quantity + product.quantity)
        return products_quantity
    
    def subtotal(self) -> float:
        subtotal = 0.00
        for product in self.client.basket.product_basket.all():
            subtotal = float(subtotal) + float(product.quantity * product.product.price)
            
        return subtotal
    
    def __str__(self) -> str:
        return f"{self.client.email} {_(' Basket')}"
    
""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This model its the many to many relationship, we need the basket of the  │
  │ client, the product and how much of this                                 │
  │ product                                                                  │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class ProductBasket(models.Model):
    basket = ParentalKey('basket.Basket', on_delete = models.CASCADE, related_name = 'product_basket')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='basket_product')
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
    
    panels = [
        SnippetChooserPanel('product'),
        FieldPanel('quantity')
    ]
    
    class Meta:
        unique_together = ('basket', 'product')
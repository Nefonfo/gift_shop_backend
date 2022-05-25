from django.db import models

from modelcluster.models import ClusterableModel
from modelcluster.models import ParentalKey

from django.utils.translation import ugettext_lazy as _

from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel

from registration.models import User

# Create your models here.
class ShippmentMethod(models.Model):
    name = models.CharField(max_length=70, verbose_name=_('Name'))
    days = models.IntegerField(verbose_name=_('Day to deliver'))


@register_snippet
class Order(ClusterableModel, models.Model):
    
    class ShipMethod(models.TextChoices):
        STORE = 'STORE', _('Deliver on Store')
        DHL = 'DHL', _('Deliver on DHL')
    
    class PayMethod(models.TextChoices):
        STORE = 'STORE', _('Deliver on Store')
        MERCADOLIBRE = 'ML', _('MERCADOLIBRE')
    
    class PayStatus(models.TextChoices):
        STORE = 'STORE', _('Pay on Store')
        SUCESS = 'SUCCESS', _('Payed')
        DECLINED = 'DECLINED', _('Declined')
        PENDING = 'PENDING', _('Pending')
        
    class OrderStatus(models.TextChoices):
        PENDING = 'STORE', _('Pay on Store')
        PLEASE_CONTACT = 'PLEASE_CONTACT', _('Please call, we need more information')
        FULLFILLED = 'FULLFILLED', _('Shipped')
        DELIVER = 'DELIVER', _('Deliver')
    
    client = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name=_('Client'))
    address = models.TextField(verbose_name=_('Address'))
    sub_total = models.FloatField(verbose_name=_('Sub Total'))
    discount = models.FloatField(verbose_name=_('Discount'), default= 0.0, blank=True)
    pay_method =  models.CharField(
        max_length=20,
        choices=PayMethod.choices,
        default=PayMethod.STORE,
        verbose_name=_('Payment Method')
    )
    pay_track = models.TextField(verbose_name=_('Pay Tracking'), null = True, blank=True)
    pay_status = models.CharField(
        max_length=20,
        choices=PayStatus.choices,
        default=PayStatus.STORE,
        verbose_name=_('Pay Status')
    )
    order_status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
        verbose_name=_('Order Status')
    )
    ship_method = models.CharField(
        max_length=20,
        choices=ShipMethod.choices,
        default=ShipMethod.STORE,
        verbose_name=_('Shipping Method')
    ) 
    track_number = models.TextField(verbose_name=_('Track Number'), null = True, blank=True)
    
    panels = [
        SnippetChooserPanel('client'),
        InlinePanel('product_order', label = 'products'),
        FieldPanel('address'),
        FieldPanel('sub_total'),
        FieldPanel('discount'),
        FieldPanel('pay_method'),
        FieldPanel('pay_track'),
        FieldPanel('pay_status'),
        FieldPanel('order_status'),
        FieldPanel('ship_method'),
        FieldPanel('track_number'),
    ]
    
    def total(self):
        return self.sub_total - self.discount
    
class ProductOrder(models.Model):
    order = ParentalKey('order.Order', on_delete = models.CASCADE, related_name = 'product_order')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='order_product')
    price = models.FloatField(verbose_name=_('Price'))
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
    
    panels = [
        SnippetChooserPanel('product'),
        FieldPanel('price'),
        FieldPanel('quantity')
    ]
    
    class Meta:
        unique_together = ('order', 'product')
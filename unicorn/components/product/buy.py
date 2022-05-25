from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from django_unicorn.components import UnicornView

from wagtail.images.api.fields import ImageRenditionField
from basket.models import ProductBasket

from product.models import Product

class BuyView(UnicornView):
    
    button_title = None
    status_response = None
    product_id = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button_title = kwargs.get('button_title')
        self.product_id = kwargs.get('product_id')
    
    def add_product(self):
        product = Product.objects.get(id = self.product_id)
        if product.stock > 0 and product.available:
            product.stock = product.stock - 1
            product.save()
            if self.request.user.basket.product_basket.filter(product__id = product.id).exists():
                product_in_cart = self.request.user.basket.product_basket.filter(product__id = product.id).first()
                product_in_cart.quantity = product_in_cart.quantity + 1
                product_in_cart.save()
                self.status_response = str(_('Product added to basket'))
            else:
                new_product_in_cart = ProductBasket()
                new_product_in_cart.basket = self.request.user.basket
                new_product_in_cart.quantity = 1
                new_product_in_cart.product = product
                new_product_in_cart.save()
                self.status_response = str(_('Added another to basket'))
        else:
            self.status_response = str(_('Product not available'))
        
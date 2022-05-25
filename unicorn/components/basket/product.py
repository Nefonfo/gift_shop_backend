from django.shortcuts import redirect
from django_unicorn.components import UnicornView
from django.urls import reverse

from product.models import Product

class ProductView(UnicornView):
    product_url = ''
    product_id = None
    product_name = ''
    product_image = ''
    product_quantity = ''
    product_price = ''
    extra_class=None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_url = kwargs.get('product_url')
        self.product_id = kwargs.get('product_id')
        self.product_name = kwargs.get('product_name')
        self.product_image = kwargs.get('product_image')
        self.product_quantity = kwargs.get('product_quantity')
        self.product_price = kwargs.get('product_price')
        self.extra_class = kwargs.get('extra_class')

    def add(self):
        product = Product.objects.get(id = self.product_id)
        if product.stock > 0 and product.available:
            product.stock = product.stock - 1
            product.save()
            product_in_cart = self.request.user.basket.product_basket.filter(product__id = product.id).first()
            product_in_cart.quantity = product_in_cart.quantity + 1
            product_in_cart.save()
            self.product_quantity = self.product_quantity + 1
            
    def reduce(self):
        product = Product.objects.get(id = self.product_id)
        product_in_cart = self.request.user.basket.product_basket.filter(product__id = product.id).first()
        if product_in_cart.quantity > 1:
            product.stock = product.stock + 1
            product.save()
            product_in_cart.quantity = product_in_cart.quantity - 1
            product_in_cart.save()
            self.product_quantity = self.product_quantity - 1

    def delete(self):
        product = Product.objects.get(id = self.product_id)
        product_in_cart = self.request.user.basket.product_basket.filter(product__id = product.id).first()
        product_in_cart.delete()
        
        return redirect(reverse('basket:user'))
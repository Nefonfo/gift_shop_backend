from django_unicorn.components import UnicornView
from django.db.models import Sum

class NavbarIconView(UnicornView):
    
    products_quantity = 0
    subtotal = 0
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.view_cart()
    
    
    def view_cart(self):
        self.products_quantity = 0;
        self.subtotal = 0.00;
        for product in self.request.user.basket.product_basket.all():
            self.products_quantity = int(self.products_quantity + product.quantity)
            self.subtotal = float(self.subtotal) + float(product.quantity * product.product.price)

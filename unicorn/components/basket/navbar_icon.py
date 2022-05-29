from django_unicorn.components import UnicornView
from django.db.models import Sum

from basket.models import Basket

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This class its a reactive view that its rendered as a compononent in     │
  │ all the views (cart icon) and shows the quantity of products and the     │
  │ total                                                                    │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class NavbarIconView(UnicornView):
    
    products_quantity = 0
    subtotal = 0
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.view_cart()
    
    
    def view_cart(self):
        basket = Basket.objects.get_or_create(client = self.request.user)
        self.products_quantity = basket.quantity();
        self.subtotal = basket.subtotal();
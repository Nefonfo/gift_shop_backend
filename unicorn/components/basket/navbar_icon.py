from django_unicorn.components import UnicornView
from django.db.models import Sum

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
        self.products_quantity = self.request.user.basket.quantity();
        self.subtotal = self.request.user.basket.subtotal();
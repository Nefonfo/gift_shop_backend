from django_unicorn.components import UnicornView


class SubtotalView(UnicornView):
    
    subtotal = 0
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.get_subtotal()
        
    def get_subtotal(self):
        self.subtotal = 0
        for product in self.request.user.basket.product_basket.all():
            self.subtotal = self.subtotal + float(product.quantity * product.product.price)
from django_unicorn.components import UnicornView


""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This model creates a reactive component to recharge the subtotal of the  │
  │ basket                                                                   │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class SubtotalView(UnicornView):
    
    subtotal = 0
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.get_subtotal()
        
    def get_subtotal(self):
        self.subtotal = self.request.user.basket.subtotal()
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from basket.models import Basket


""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This view will display all products in the user basket (login required)  │
  └──────────────────────────────────────────────────────────────────────────┘
 """
# Create your views here.
class BasketListView(LoginRequiredMixin, ListView):
    model = Basket
    context_object_name = 'basket'
    template_name = 'basket/basket_list_view.html'
    
    def get_queryset(self):
        return self.model.objects.get(client = self.request.user)

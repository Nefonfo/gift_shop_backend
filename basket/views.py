from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_unicorn.components import UnicornView

from basket.models import Basket

# Create your views here.
class BasketListView(LoginRequiredMixin, ListView):
    model = Basket
    context_object_name = 'basket'
    template_name = 'basket/basket_list_view.html'
    
    def get_queryset(self):
        return self.model.objects.get(client = self.request.user)

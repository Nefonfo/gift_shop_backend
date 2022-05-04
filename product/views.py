from http import client
from django.shortcuts import render
from django.views.generic import TemplateView

from product.models import Product
from basket.models import Basket
# Create your views here.
class ProductIndexView(TemplateView):
    template_name = 'product/product_index.html'
    
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['index_products'] = Product.objects.all().order_by('created_at')[:10]
        if self.request.user.is_authenticated:    
            context_data['user_basket'] = Basket.objects.get_or_create(client = self.request.user)
        else:
            context_data['user_basket'] = None
        return context_data
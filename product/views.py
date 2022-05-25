from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from product.forms import ProductSearchForm

from django_unicorn.components import UnicornView

from product.models import Product
from basket.models import Basket
# Create your views here.
class ProductIndexView(TemplateView):
    template_name = 'product/product_index.html'
    
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['index_products'] = Product.objects.filter(Q(available = True) & Q(stock__gt = 0)).order_by('-created_at')[:10]
        if self.request.user.is_authenticated:    
            context_data['user_basket'] = Basket.objects.get_or_create(client = self.request.user)
        else:
            context_data['user_basket'] = None
        return context_data
    
class ProductListView(ListView):
    model = Product
    paginate_by = 10
    context_object_name = 'products'
    ordering = ['-created_at']
    form_class = ProductSearchForm
    template_name = 'product/product_list_view.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = Product.tags.all()
        data['search_form'] = ProductSearchForm()
        return data
    
    def get_queryset(self):
        form = self.form_class(self.request.GET)
        qs_filter = Q(available = True)
        qs_filter &= Q(stock__gt = 0)
        if form.is_valid():
            if form.cleaned_data['name']:
                qs_filter &= Q(name__icontains = form.cleaned_data['name'])
            if form.cleaned_data['price']:
                qs_filter &= Q(price__lte = form.cleaned_data['price'])
            if form.cleaned_data['category']:
                qs_filter &= Q(tags__name__in = [form.cleaned_data['category'], ])
        qs = self.model.objects.filter(qs_filter).order_by('-created_at')
        return qs
    
class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    slug_field = 'url'
    slug_url_kwarg = 'url'
    template_name = 'product/product_detail_view.html'

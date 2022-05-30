from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from product.forms import ProductSearchForm
from wagtail.search.backends import get_search_backend
from product.models import Product

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This model its to create the main index view, it will show the recent    │
  │ products                                                                 │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class ProductIndexView(TemplateView):
    template_name = 'product/product_index.html'
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['index_products'] = Product.objects.filter(Q(available = True) & Q(stock__gt = 0)).order_by('-created_at')[:10]
        return context_data

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This page will list the products paginated by 10 and order by creation.  │
  │ It will be posible to filter by a form with the parameters: name, price  │
  │ and category                                                             │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class ProductListView(ListView):
    model = Product
    paginate_by = 9
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
        qs = self.model.objects.none()
        qs_filter = Q(available = True)
        qs_filter &= Q(stock__gt = 0)
        s = get_search_backend()
        if form.is_valid():
            if form.cleaned_data['price']:
                qs_filter &= Q(price__lte = form.cleaned_data['price'])
            if form.cleaned_data['category']:
                qs_filter &= Q(tags__name__in = [form.cleaned_data['category'], ])
            if form.cleaned_data['name']:
                qs = s.search(form.cleaned_data['name'], self.model.objects.filter(qs_filter).order_by('-created_at'))
            else:
                qs = self.model.objects.filter(qs_filter).order_by('-created_at')
        return qs
    
    

    
""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This view will show the product details, will be need the slug name      │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    slug_field = 'url'
    slug_url_kwarg = 'url'
    template_name = 'product/product_detail_view.html'

from django.urls import path

from .views import (
    ProductIndexView,
    ProductListView,
    ProductDetailView,
)

products_patterns = ([
    path('', ProductIndexView.as_view(), name = 'index'),
    path('store/', ProductListView.as_view(), name="store"),
    path('store/<slug:url>', ProductDetailView.as_view(), name="detail")
], 'products')
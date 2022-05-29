from django.urls import path

from .views import (
    ProductIndexView,
    ProductListView,
    ProductDetailView,
)


""" 
  ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │ This file is to have the variable for urls located in address app and this will be imported in setting base.py                                                                                                                   │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
 """
 
products_patterns = ([
    path('', ProductIndexView.as_view(), name = 'index'),
    path('store/', ProductListView.as_view(), name="store"),
    path('store/<slug:url>', ProductDetailView.as_view(), name="detail")
], 'products')
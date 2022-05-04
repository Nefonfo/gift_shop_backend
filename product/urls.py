from django.urls import path

from .views import (
    ProductIndexView
)

products_patterns = ([
    path('', ProductIndexView.as_view(), name = 'index')
], 'products')
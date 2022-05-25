from django.urls import path

from .views import (
    BasketListView,
)

basket_patterns = ([
    path('', BasketListView.as_view(), name = 'user'),
], 'basket')
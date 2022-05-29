from django.urls import path

from .views import (
    BasketListView,
)

""" 
  ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │ This file is to have the variable for urls located in address app and this will be imported in setting base.py                                                                                                                   │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
 """
basket_patterns = ([
    path('', BasketListView.as_view(), name = 'user'),
], 'basket')
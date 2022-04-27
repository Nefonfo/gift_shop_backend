from django.urls import path

from .views import (
    ClientAddressCreateView,
    ClientAddressListView,
    ClientAddressUpdateView,
    ClientAddressDeleteView
)

address_patterns = ([
    path('', ClientAddressListView.as_view(), name='view'),
    path('add/', ClientAddressCreateView.as_view(), name='add'),
    path('<pk>/update/', ClientAddressUpdateView.as_view(), name='update'),
    path('<pk>/delete/', ClientAddressDeleteView.as_view(), name='delete')
], 'address')
from django.urls import path

from .views import (
    UserProfileView,
    UserEditProfileView,
    UserSignUpView
)

""" 
  ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │ This file is to have the variable for urls located in address app and this will be imported in setting base.py                                                                                                                   │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
 """
profile_patterns = ([
    path('', UserProfileView.as_view(), name='view'),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('edit/', UserEditProfileView.as_view(), name='edit')
    
], 'profile')
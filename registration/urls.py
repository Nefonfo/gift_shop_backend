from django.urls import path

from .views import (
    UserProfileView,
    UserEditProfileView,
    UserRegisterView
)

profile_patterns = ([
    path('', UserProfileView.as_view(), name='view'),
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('edit/', UserEditProfileView.as_view(), name='edit')
    
], 'profile')
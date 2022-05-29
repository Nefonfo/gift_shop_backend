import profile
from django.db.utils import IntegrityError
from django.core.files.images import ImageFile
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from wagtail.users.forms import UserEditForm, UserCreationForm
from wagtail.users.models import UserProfile

from .models import User

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Internal model to override the user edit model form, because we          │
  │ need to login with email and not with                                    │
  │ username                                                                 │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class CustomUserEditForm(UserEditForm):
    email = forms.EmailInput(attrs={'label':  _('Email'), 'required': True})

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Internal model to override the user create model form, because we        │
  │ need to login with email and not with                                    │
  │ username                                                                 │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailInput(attrs={'label':  _('Email'), 'required': True})
    
""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ this form is used to registration model                                  │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class UserRegisterForm(UserCreationForm):
    class Meta:
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2',]
        model = get_user_model()
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields.pop('is_superuser')

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ this form model helps to edit the user profile (avatar included)         │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class UserProfileForm(forms.Form):
    avatar = forms.ImageField(required = False, label = _('Avatar'))
    email = forms.EmailField(required = True, label = _('Email'))
    first_name = forms.CharField(min_length = 2, max_length = 150, required = True, label = _('First Name'))
    last_name = forms.CharField(min_length = 2, max_length = 150, required = True, label = _('Last Name'))

    def save_user(self, user):
        form_data = self.cleaned_data
        user_with_email = User.objects.filter(email = form_data['email'])
        if user_with_email.exists() and user.email != form_data['email']:
            raise IntegrityError(_('The email is alredy used, recover your account'))
        else:
            user.email = form_data['email']
            user.first_name = form_data['first_name']
            user.last_name = form_data['last_name']
            user.save()
        if form_data['avatar'] is not None:
            user_profile = UserProfile.objects.get(user = user)
            image = ImageFile(form_data['avatar'], name = form_data['avatar'].name)
            user_profile.avatar = image
            user_profile.save()

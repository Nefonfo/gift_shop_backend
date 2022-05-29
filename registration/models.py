from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

from wagtail.snippets.models import register_snippet
from wagtail.search import index

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ this model its for override the user manager model (we need to change    │
  │ the login method to email instead of username), the user manager its     │
  │ the object that we use when we call                                      │
  │ <Model>.objects.<query>                                                  │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

# Create your models here.

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This model will replace the default user model that use django in        │
  │ django.contrib.auth.models, and here will change the object              │
  │ objects                                                                  │
  └──────────────────────────────────────────────────────────────────────────┘
 """
@register_snippet
class User(index.Indexed, AbstractUser):
    username = None
    email = models.EmailField(verbose_name=_('Email Address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
    

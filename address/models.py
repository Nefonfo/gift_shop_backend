from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator, RegexValidator

from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index

from registration.models import User

# Create your models here.
@register_snippet
class ClientAddress(index.Indexed, models.Model):
    client = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name=_('Client'))
    street = models.TextField(verbose_name=_('Street'))
    ext_number = models.CharField(max_length=10, verbose_name = _('External Number'))
    int_number = models.CharField(max_length=10, verbose_name = _('Internal Number'), null = True, blank = True)
    colony = models.CharField(max_length=100, verbose_name = _('Colony'))
    municipality = models.CharField(max_length=100, verbose_name=_('Municipality'), null = True, blank = False)
    country = models.CharField(max_length=100, verbose_name = _('Country'))
    zip_code = models.IntegerField(verbose_name = _('Zip Code'))
    additional_notes = models.CharField(max_length=255, verbose_name = _('Additional Notes'), null = True, blank = True)
    phone_number = models.CharField(max_length=10, verbose_name = _('Phone Number'), null = True, blank = False, validators=[MinLengthValidator(10), RegexValidator(
        regex='^\d{10}$',
        message=_('The number must be of 10 digits'),
        code='invalid_phone_number'
    )])
    
    panels = [
        SnippetChooserPanel('client'),
        FieldPanel('street'),
        FieldPanel('ext_number'),
        FieldPanel('int_number'),
        FieldPanel('colony'),
        FieldPanel('municipality'),
        FieldPanel('country'),
        FieldPanel('zip_code'),
        FieldPanel('additional_notes'),
        FieldPanel('phone_number'),
    ]
    
    search_fields = [
        index.RelatedFields('client', [
            index.SearchField('email'),
            index.SearchField('fist_name'),
            index.SearchField('last_name')
        ]),
    ]
    
    def __str__(self) -> str:
        return '{}, {}, {}, {}, {}, {}'.format(self.street, self.ext_number, self.colony, self.municipality, self.country, self.zip_code)
    
    

from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.contrib import messages

from .models import ClientAddress
# Create your views here.

class ClientAddressListView(LoginRequiredMixin, ListView):
    template_name = "address/client_address_list_view.html"
    model = ClientAddress
    context_object_name = 'client_address_list'

    def get_queryset(self):
        return ClientAddress.objects.filter(client = self.request.user)
    
class ClientAddressCreateView(LoginRequiredMixin, CreateView):
    template_name = "address/client_address_create_view.html"
    model = ClientAddress
    fields = ['street', 'ext_number', 'int_number', 'colony', 'municipality', 'country', 'zip_code', 'phone_number', 'additional_notes']
    
    def form_valid(self, form):
        form.instance.client = self.request.user
        return super(ClientAddressCreateView, self).form_valid(form)
    
    def get_success_url(self) -> str:
        messages.success(self.request, _('Created Successful'))
        return reverse('address:view')
    
class ClientAddressUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "address/client_address_update_view.html"
    model = ClientAddress
    fields = ['street', 'ext_number', 'int_number', 'colony', 'municipality', 'country', 'zip_code', 'phone_number', 'additional_notes']
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.client != self.request.user:
            return redirect(reverse('address:view'))
        return super(ClientAddressUpdateView, self).dispatch(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        messages.success(self.request, _('Updated Successful'))
        return reverse('address:view')
    
class ClientAddressDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "address/client_address_delete_view.html"
    model = ClientAddress
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.client != self.request.user:
            return redirect(reverse('address:view'))
        return super(ClientAddressDeleteView, self).dispatch(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        messages.success(self.request, _('Delete Successful'))
        return reverse('address:view')
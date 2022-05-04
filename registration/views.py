from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

from wagtail.users.models import UserProfile

from .models import User
from .forms import UserRegisterForm, UserProfileForm

# Create your views here.

class UserSignUpView(TemplateView):
    template_name = 'registration/user_signup.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = UserRegisterForm()
        context['sign_form'] = AuthenticationForm()
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.POST.get('action', None ) == 'register':
            form = UserRegisterForm(request.POST)
            form.save()
            messages.success(request, _('Created Successful'))
        elif request.POST.get('action', None) == 'login':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, _('Welcome'))
                    return HttpResponseRedirect(reverse('profile:view'))
                else:
                    print('paso')
                    messages.error(request, _('User or password incorrect'))
            else:
                messages.error(request, _('User or password incorrect'))
            
        return self.render_to_response(context)
class UserProfileView(LoginRequiredMixin, TemplateView):

    template_name = 'registration/user_profile.html'

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return redirect(reverse('wagtailadmin_home'))
        elif self.request.user.first_name == '' or self.request.user.last_name == '':
            messages.warning(self.request, _('You need to update your First Name and/or Last Name'))
            return redirect(reverse('profile:edit'))
        else:
            return super().render_to_response(context, **response_kwargs)

class UserEditProfileView(LoginRequiredMixin, FormView):
    template_name = 'registration/user_profile_edit.html'
    form_class = UserProfileForm

    def form_valid(self, form):
        try:
            form.save_user(User.objects.get(email = self.request.user))
            messages.success(self.request, _('Updated Successful'))
        except Exception as e:
            messages.error(self.request, _('Error: ') + str(e))
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('profile:view')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {
            'email': self.request.user.email,
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name
        }
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_avatar'] = UserProfile.get_for_user(User.objects.get(email = self.request.user)).avatar
        return context
    
class UserRegisterView(CreateView):
    template_name = 'registration/user_registration.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
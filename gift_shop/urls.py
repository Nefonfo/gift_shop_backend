from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.views.generic import RedirectView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

from registration.urls import profile_patterns
from address.urls import address_patterns
from product.urls import products_patterns
from basket.urls import basket_patterns

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('search/', search_views.search, name='search'),

]


if settings.DEBUG:
    import debug_toolbar
    
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(products_patterns)),
    path("basket/", include(basket_patterns)),
    path("accounts/login/", RedirectView.as_view(pattern_name = 'profile:signup'), name='login_redirect'),
    path("accounts/register/", RedirectView.as_view(pattern_name = 'profile:signup'), name='register_redirect'),
    path("accounts/profile/", include(profile_patterns)),
    path("accounts/address/", include(address_patterns)),
    path("accounts/", include('django.contrib.auth.urls')),
    path("unicorn/", include("django_unicorn.urls")),
    path("cms/", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]

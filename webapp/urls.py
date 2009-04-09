from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    # Example:
    # (r'^webapp/', include('webapp.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
     {'template_name': 'admin/login.html'}, name='login'),

    url(r'^accounts/logout/$', 'uploads.views.logout', name='logout'),

    (r'^$', 'uploads.views.index'),

    (r'^uploads/', include('uploads.urls')),
)

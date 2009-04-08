from django.conf.urls.defaults import *

from uploads import views

urlpatterns = patterns(
    '',

    url(r'^$', views.index, name='uploads-list'),
    url(r'^form/$', views.form, name='uploads-form'),
    url(r'^show/(?P<id>\d+)/$', views.show, name='uploads-show'),
    url(r'^get/(?P<download_key>.+)/$', views.get, name='uploads-get'),
)

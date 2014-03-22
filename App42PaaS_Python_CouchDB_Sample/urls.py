from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','sample.views.index'),
    url(r'^detail', 'sample.views.detail'),
    url(r'^show', 'sample.views.show'),
)

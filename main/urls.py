from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('main',
    url(r'^$', 'views.index'),
)

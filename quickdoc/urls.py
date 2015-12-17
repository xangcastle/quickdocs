# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('quickdocs.views',
    url(r'^$', 'consulta', name='consulta'),
    url(r'^expediente/(?P<id>.*)/$', 'ver_expediente', name='ver_expediente'),
)
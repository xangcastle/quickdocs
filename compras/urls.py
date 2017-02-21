from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('compras.views',
  url(r'^asignar_cuenta/$', 'asignar_cuenta', name='asignar_cuenta'),
)

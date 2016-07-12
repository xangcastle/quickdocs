from django.conf.urls import *
from .views import *


urlpatterns = patterns('contabilidad.views',
    url(r'^inicio/$', index.as_view(),
        name='inicio'),
    url(r'^comprobantes/$', comprobantes.as_view(),
        name='comprobantes'),
    url(r'^datos_comprobante/$', 'datos_comprobante',
        name='datos_comprobante'),
    url(r'^tableComprobante/$', 'tableComprobante',
        name='tableComprobante'),
    url(r'^autocomplete_cuenta/$', 'autocomplete_cuenta',
        name='autocomplete_cuenta'),
)
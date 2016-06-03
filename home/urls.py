from django.conf.urls import *
from .views import *


urlpatterns = patterns('home.views',
    url(r'^expediente/$', expediente.as_view(),
        name='expediente'),
    url(r'^datos_expediente/$', 'datos_expediente',
        name='datos_expediente'),
    url(r'^tableExpediente/$', 'tableExpediente',
        name='tableExpediente'),
)
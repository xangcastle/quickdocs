from django.conf.urls import *
from .views import *


urlpatterns = patterns('',
    url(r'^expediente/$', expediente.as_view(),
        name='expediente'),
)
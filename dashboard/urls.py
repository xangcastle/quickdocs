from django.conf.urls import *
from .views import *


urlpatterns = patterns('dashboard.views',
    url(r'^slide/$', slide.as_view(),
        name='slide'),
)

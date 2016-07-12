from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from home.views import index
from segdel.views import index as segdel

urlpatterns = patterns('',
    url(r'^$', index.as_view(), name='home'),
    url(r'^contabilidad/', include('contabilidad.urls')),
    url(r'^segdel/', segdel.as_view(), name='segdel'),
    url(r'^home/', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^adminactions/', include('adminactions.urls')),
    url(r'^digitalizacion/', include('digitalizacion.urls')),
    url(r'^quickdoc/', include('quickdoc.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

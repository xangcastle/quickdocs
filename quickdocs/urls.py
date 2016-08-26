from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'quickdoc.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^adminactions/', include('adminactions.urls')),
    url(r'^digitalizacion/', include('digitalizacion.urls')),
    url(r'^quickdoc/', include('quickdoc.urls')),
    url(r'^facturacion/', include('facturacion.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from .models import *


class documento_admin(admin.TabularInline):
    model = Documento
    extra = 0


class indice_admin(admin.ModelAdmin):
    list_display = ('indice', 'descripcion')
    search_fields = ('indice', 'descripcion')
    list_filter = ('indice_superior',)
admin.site.register(Indice, indice_admin)


class expediente_admin(admin.ModelAdmin):
    list_display = ('codigo', 'identificacion', 'nombre', 'tipodoc', 'ver_expediente')
    search_fields = ('codigo', 'identificacion', 'nombre')
    list_filter = ('tipodoc',)
    inlines = [documento_admin]
admin.site.register(Expediente, expediente_admin)
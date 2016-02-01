from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class expediente_natural_admin(admin.TabularInline):
    model = documento_natural
    extra = 0


class expediente_juridico_admin(admin.TabularInline):
    model = documento_juridico
    extra = 0


class indice_admin(ImportExportModelAdmin):
    list_display = ('indice', 'descripcion')
    search_fields = ('indice', 'descripcion')
    list_filter = ('indice_superior',)
admin.site.register(Indice, indice_admin)


class expediente_admin(admin.ModelAdmin):
    list_display = ('codigo', 'identificacion', 'nombre', 'tipodoc',
        'ver_expediente')
    search_fields = ('codigo', 'identificacion', 'nombre')
    list_filter = ('tipodoc',)
    inlines = [expediente_natural_admin, expediente_juridico_admin]
admin.site.register(Expediente, expediente_admin)
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class paquete_admin(ImportExportModelAdmin):
    list_display = ('num_paquete', 'cf_cliente', 'direccion', 'emision', 'entregado')
    list_filter = ('entregado', )
    search_fields = ('num_paquete', 'cf_cliente')

admin.site.register(Paquete, paquete_admin)

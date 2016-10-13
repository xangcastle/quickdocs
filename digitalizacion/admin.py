from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
import os
from django.http.response import HttpResponse
from django.core.servers.basehttp import FileWrapper


def download_file(path):
    if not os.path.exists(path):
        return HttpResponse('Sorry. This file is not available.')
    else:
        response = HttpResponse(
            FileWrapper(file(path)),
            content_type='application/force-download')
        response['Content-Disposition'] = \
        'attachment; filename=%s' % os.path.basename(path)
        return response


class empleado_admin(ImportExportModelAdmin):
    list_display = ('idempleado', 'nombre', 'cedula', 'gerencia', 'localidad',
        'link_ecuenta')
    list_filter = ('localidad', )
    search_fields = ('idempleado', 'nombre', 'cedula')
    actions = ['action_exportar']

    def action_exportar(self, request, queryset):
        carpeta = queryset[0].export_path()
        cmd = "cd %s && rm *.pdf" % carpeta
        os.system(cmd)
        numero_pagina = 1
        for e in queryset:
            e.exportar_ecuenta(str(numero_pagina).zfill(6) + '.pdf')
            numero_pagina += 1
        if numero_pagina > 1:
            cmd = "cd %s && mkdir tm && mv *.pdf tm/" % carpeta
            os.system(cmd)
            cmd = "cd %s && pdftk tm/*.pdf cat output ecuenta.pdf && rm -rf tm"\
             % carpeta
            os.system(cmd)
        return download_file(os.path.join(carpeta, 'ecuenta.pdf'))


class indexacion_admin(ImportExportModelAdmin):
    date_hierarchy = "fecha"
    list_display = ('fecha', 'carga_manual',
        'carpeta', 'path')
    fields = ('archivos', 'make_ocr')
    actions = ['action_indexar']

    def action_indexar(self, request, queryset):
        for obj in queryset:
            indexar_carpeta(obj)
    action_indexar.short_description = \
    'Iniciar proceso de indexacion automatica'

admin.site.register(Indexacion, indexacion_admin)


admin.site.register(Empleado, empleado_admin)

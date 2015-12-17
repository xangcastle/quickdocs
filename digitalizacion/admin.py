from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import math
from metropolitana.models import exportar_media_temp, Paquete
from .api import indexar_carpeta
import os
from django.http.response import HttpResponse
from django.core.servers.basehttp import FileWrapper


def download_file(path):
    if not os.path.exists(path):
        return HttpResponse('Sorry. This file is not available.')
    else:
        response = HttpResponse(FileWrapper(file(path)), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(path)
        return response


class pod_admin(admin.ModelAdmin):
    list_display = ('factura', 'contrato', 'consecutivo', 'cliente',
        'ciclo', 'mes', 'entrega', 'comprobante')
    list_editable = ('comprobante',)
    search_fields = ('factura', 'contrato', 'cliente', 'barra')
    list_filter = ('ano', 'mes', 'ciclo', 'entrega', 'departamento', 'archivo',
        'entrega_numero')
    actions = ['action_exportar']

    def action_exportar(self, request, queryset):
        ps = Paquete.objects.filter(id__in=queryset.values_list('id',
        flat=True))
        exportar_media_temp(ps)
    action_exportar.short_description = 'exportar pdf de pods seleccionados'


class impresion_admin(ImportExportModelAdmin):
    date_hierarchy = 'fecha_verificacion'
    list_display = ('consecutivo', 'paquete', 'cliente', 'user',
        'archivo', 'fecha_verificacion')
    list_per_page = 1200
    list_filter = ('user', 'archivo')
    search_fields = ('paquete__cliente', 'paquete__factura', 'paquete__barra',
        'paquete__contrato')
    actions = ['generar_comprobantes']

    def generar_comprobantes(self, request, queryset):
        paginas = []
        id_unico = False
        if queryset.count() == 1:
            id_unico = True
        for q in queryset:
            c = Paquete.objects.get(id=q.paquete.id)
            c.orden_impresion = q.consecutivo
            c.save()
        comprobantes = Paquete.objects.filter(
            id__in=queryset.order_by('consecutivo').values_list('paquete',
                flat=True)).order_by('archivo', 'orden_impresion')
        if comprobantes:
            pagina = {'comprobantes': []}
            tp = int(math.ceil(comprobantes.count() / 6.0))
            for p in range(0, tp):
                for i in range(p, int(tp * 6), tp):
                    try:
                        pagina['comprobantes'].append(comprobantes[i])
                    except:
                        pagina['comprobantes'].append(Paquete())
                if len(pagina['comprobantes']) == 6:
                    paginas.append(pagina)
                    pagina = {'comprobantes': []}
            if len(pagina['comprobantes']) > 0:
                paginas.append(pagina)
        ctx = {'queryset': queryset, 'id_unico': id_unico, 'paginas': paginas}
        return render_to_response('metropolitana/comprobante.html',
            ctx, context_instance=RequestContext(request))
    generar_comprobantes.short_description = \
    "Generar comprobantes selecionados"


admin.site.register(Pod, pod_admin)
admin.site.register(Impresion, impresion_admin)
admin.site.register(import_paquete, ImportExportModelAdmin)


class indexacion_admin(ImportExportModelAdmin):
    date_hierarchy = "fecha"
    list_display = ('fecha', 'total', 'resumen_por_ciclo', 'carga_manual')
    fields = ('archivos', 'make_ocr')

    def save_model(self, request, obj, form, change):
        indexar_carpeta(obj)
admin.site.register(Indexacion, indexacion_admin)


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


admin.site.register(Empleado, empleado_admin)
admin.site.register(Tar)
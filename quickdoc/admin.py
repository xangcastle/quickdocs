from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.template.context import RequestContext
from django.shortcuts import render_to_response


class producto_cliente_admin(admin.TabularInline):
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)
    model = producto_cliente
    extra = 0


class expediente_admin(admin.ModelAdmin):
    list_display = ('codigo', 'identificacion', 'nombre', 'tipo',
        'ver_expediente')
    search_fields = ('codigo', 'identificacion', 'nombre')
    list_filter = ('tipo',)
    inlines = [producto_cliente_admin]
    actions = ['generar_index', 'generar_docs']

    def generar_index(self, request, queryset):
        indices = []
        for obj in queryset:
            for i in obj.indices():
                indices.append(i)
        ctx = {'indices': indices}
        return render_to_response('quickdocs/indices.html',
            ctx, context_instance=RequestContext(request))

    def generar_docs(self, request, queryset):
        for obj in queryset:
            obj.generar_documentos()

admin.site.register(Expediente, expediente_admin)


class producto_admin(ImportExportModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')

admin.site.register(Producto, producto_admin)


class indice_admin(ImportExportModelAdmin):
    list_display = ('code', 'indice', 'name', 'tipo')
    search_fields = ('indice', 'code', 'name')
    list_filter = ('tipo',)
admin.site.register(Indice, indice_admin)


class importacion_admin(ImportExportModelAdmin):
    list_display = ('codigo', 'nombre', 'identificacion', 'producto', 'numero')
    list_filter = ('producto', 'tipo')
    search_fields = ('codigo', 'nombre', 'identificacion', 'numero')
    actions = ['action_integrar']

    def action_integrar(self, request, queryset):
        for obj in queryset:
            obj.integrar()
    action_integrar.short_description = \
    "integrar al sistema los registros seleccionados"

admin.site.register(Importacion, importacion_admin)


class documento_admin(admin.ModelAdmin):
    list_display = ('code', 'expediente', 'numero', 'indice', 'producto',
        'documento')
    list_editable = ('documento',)
    search_fields = ('code',)

admin.site.register(Documento, documento_admin)
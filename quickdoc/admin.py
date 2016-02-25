from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class expediente_natural_admin(admin.TabularInline):
    classes = ('grp-collapse grp-open',)
    model = documento_natural
    extra = 0


class expediente_juridico_admin(admin.TabularInline):
    classes = ('grp-collapse grp-open',)
    model = documento_juridico
    extra = 0


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
    inlines = [producto_cliente_admin, expediente_juridico_admin,
        expediente_natural_admin]
admin.site.register(Expediente, expediente_admin)


class producto_admin(ImportExportModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')

admin.site.register(Producto, producto_admin)


class indice_admin(ImportExportModelAdmin):
    list_display = ('indice', 'descripcion')
    search_fields = ('indice', 'descripcion')
    list_filter = ('indice_superior',)
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
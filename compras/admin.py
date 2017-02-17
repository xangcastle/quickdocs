from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *



class expediente_admin(admin.TabularInline):
    model = Expediente
    extra = 0
    classes = ('grp-collapse grp-open', )


class proveedor_admin(ImportExportModelAdmin):
    list_display = ('codigo', 'nombre', 'identificacion', 'r_legal', 'servicio', 'email', 'telefono')
    search_fields = ('codigo', 'codigo_cliente', 'nombre', 'identificacion', 'r_legal', 'servicio', 'email', 'telefono')
    list_filter = ('servicio', 'relacionado', 'contrato', 'activo')

    fieldsets = (
        ('', {
                'classes': ('grp-collapse grp-open', ),
                'fields': (
                            ('codigo', 'codigo_cliente'), ('nombre', 'identificacion'),
                            ('actividad', 'servicio'), ('forma_pago', 'contacto'),
                            'email', ('telefono', 'r_legal'),'direccion',
                        )
        }),
        ('Informacion Adicional', {
                'classes': ('grp-collapse grp-open', ),
                'fields': (('cuenta_cordobas', 'beneficiario_cordobas'),
                          ('cuenta_dolares', 'beneficiario_dolares'),
                          ('relacionado', 'contrato', 'activo'),
                          )
        }),
      )

    inlines = [expediente_admin,]


admin.site.register(Proveedor, proveedor_admin)

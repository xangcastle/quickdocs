from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from django.contrib.admin import site
import adminactions.actions as actions
actions.add_to_site(site)



class expediente_admin(admin.TabularInline):
    model = Expediente
    extra = 0
    classes = ('grp-collapse grp-open', )


class proveedor_admin(ImportExportModelAdmin):

    def get_queryset(self, request):
        queryset = super(proveedor_admin, self).get_queryset(request)
        usuario = request.user
        if usuario.is_superuser:
            return queryset
        else:
            return queryset.filter(usuario=usuario)

    change_form_template = "compras/proveedor.html"
    list_display = ('codigo', 'nombre', 'identificacion', 'r_legal', 'servicio', 'email', 'telefono', 'puntaje')
    search_fields = ('codigo', 'codigo_cliente', 'nombre', 'identificacion', 'r_legal', 'servicio', 'email', 'telefono')
    list_filter = ('servicio', 'relacionado', 'contrato', 'activo', 'puntaje')

    fieldsets = (
        ('', {
                'classes': ('grp-collapse grp-open', ),
                'fields': (
                            ('codigo', 'codigo_cliente'), ('nombre', 'identificacion'),
                            ('servicio', 'actividad_economica'), ('forma_pago', 'contacto'),
                            'email', ('telefono', 'r_legal'),'direccion', 'usuario'
                        )
        }),
        ('Informacion Adicional', {
                'classes': ('grp-collapse grp-open', ),
                'fields': (('cuenta_cordobas', 'beneficiario_cordobas'),
                          ('cuenta_dolares', 'beneficiario_dolares'),
                          ('relacionado', 'contrato', 'activo'),
                          ),}),
        ('Parametros de la Evaluacion', {
                'classes': ('grp-collapse grp-open evaluacion', ),
                'fields': ('importacia', 'complejidad', 'reemplazo', 'credito',
                           'anual', 'incumplimiento', 'actividad', 'recurrente',
                           'transversal', 'incidencia', 'multicontrato', 'marco', 'puntaje')
        }),
      )

    inlines = [expediente_admin,]


admin.site.register(Proveedor, proveedor_admin)

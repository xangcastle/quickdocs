from django.contrib import admin
from .models import *
import adminactions.actions as actions
from django.contrib.admin import site
actions.add_to_site(site)


class cuenta_admin(admin.ModelAdmin):
    list_display = ('code', 'name', 'tipo', 'clase', 'active')
    list_filter = ('parent', 'active')
    fields = (('code', 'name'), ('tipo', 'clase'))


class periodo_admin(admin.ModelAdmin):
    list_display = ('mes', 'ano')
    list_filter = ('ano',)

    actions = ['aperturar_saldos', 'cerrar_periodos']

    def aperturar_saldos(self, request, queryset):
        for q in queryset:
            q.aperturar_saldos()

    def cerrar_periodos(self, request, queryset):
        for q in queryset:
            q.cerrar()


class cuenta_periodo_admin(admin.ModelAdmin):
    list_display = ('cuenta', 'saldo_inicial', 'saldo_final', 'periodo')
    list_filter = ('periodo', )
    search_fields = ('cuenta__name', 'cuenta__code')


class movimiento_admin(admin.TabularInline):
    model = Movimiento


class comprobante_admin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'concepto', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('numero', 'concepto')

    inlines = [movimiento_admin, ]

admin.site.register(Cuenta, cuenta_admin)
admin.site.register(Periodo, periodo_admin)
admin.site.register(CuentaPeriodo, cuenta_periodo_admin)
admin.site.register(Comprobante, comprobante_admin)

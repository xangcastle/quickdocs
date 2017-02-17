from django.contrib import admin
from .models import *


class ArticuloInline(admin.TabularInline):
    model = Articulo
    extra = 0
    classes = ('grp-collapse', 'grp-open')


class FacturaAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_display = ('numero', 'nombre', 'identificacion', 'subtotal', 'descuento', 'iva', 'total')
    search_fields = ('numero', 'nombre', 'identificacion', 'telefono', 'email')

    fields = (('numero', 'fecha'),
             ('nombre', 'identificacion'),
             ('telefono', 'email'), 'direccion',
             ('subtotal', 'descuento', 'iva'),
             ('total', 'costo', 'utilidad'))

    inlines = [ArticuloInline, ]

    change_form_template = "ventas/factura.html"

admin.site.register(Factura, FacturaAdmin)

from django.contrib import admin
from .models import *


class person_admin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'salario', 'fecha_ingreso')
    search_fields = ('cedula', 'nombre')
    list_filter = ('salario',)
    fields = ('nombre', ('cedula', 'salario'), 'fecha_ingreso')

admin.site.register(Person, person_admin)

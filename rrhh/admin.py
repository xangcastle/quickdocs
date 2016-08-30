from django.contrib import admin
from .models import *


class person_admin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'hora')

admin.site.register(Person, person_admin)

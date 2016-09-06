from django.contrib import admin
from .models import *
from django.shortcuts import render_to_response, render
from django.core.context_processors import csrf
from django import forms
from django.contrib.admin import widgets
from datetime import datetime
from django.template import RequestContext


class person_admin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'salario', 'fecha_ingreso')
    search_fields = ('cedula', 'nombre')
    list_filter = ('salario',)
    fields = ('nombre', ('cedula', 'salario'), 'fecha_ingreso')
    actions = ['generar_planilla', 'action_fases']

    class rango_fecha(forms.Form):
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
        fecha_inicial = forms.DateField(widget=widgets.AdminDateWidget())
        fecha_final = forms.DateField(
            widget=widgets.AdminDateWidget())

    def generar_planilla(self, request, queryset):
        message = ""
        form = None
        data = {}
        data['header_tittle'] = 'Por Favor complete todos los campos'
        data['explanation'] = 'Las Siguientes personas estan incluidas en esta planilla:'
        data['action'] = 'generar_planilla'
        if 'calcular' in request.POST:
            form = self.rango_fecha(request.POST)
            if form.is_valid():
                fecha_inicial = datetime.strptime(request.POST.get('fecha_inicial', ''), "%d/%m/%Y")
                fecha_final = datetime.strptime(request.POST.get('fecha_final', ''), "%d/%m/%Y")
                data['dias'] = (fecha_final - fecha_inicial).days
                print data['dias']
                data['queryset'] = [x.pago(data['dias']) for x in queryset]
                data['header_tittle'] = 'Detalle de Pago de Planilla del periodo entre %s y %s' % (str(fecha_inicial), str(fecha_final))
                data['explanation'] = 'Se requerira Autorizacion de Gerencia para aplicar las Notas de Credito.'
                data.update(csrf(request))
                return render_to_response('rrhh/planilla_settings.html', data, RequestContext(request))

        elif 'aplicar' in request.POST:
            print "prueba 1"
            print request.POST.getlist('importe', '')
            data.update(csrf(request))
            return render_to_response('rrhh/planilla_settings.html', data, RequestContext(request))

        if not form:
            form = self.rango_fecha(
                initial={
                    '_selected_action': request.POST.getlist(
                        admin.ACTION_CHECKBOX_NAME)})
        data['queryset'] = queryset
        data['form'] = form
        data.update(csrf(request))
        self.message_user(request, message)
        return render_to_response('rrhh/planilla_settings.html', data, RequestContext(request))

    def action_fases(self, request, queryset):
        if 'fase1' and 'fase2' in request.POST:
            ctx = {'fase2':True}
            ctx.update(csrf(request))
            tpl = "rrhh/paso2.html"
        elif 'fase1' in request.POST:
            ctx = {'fase1': True}
            ctx.update(csrf(request))
            tpl = "rrhh/paso1.html"
            return render(request, tpl, ctx)
        else:
            ctx = {}
            ctx.update(csrf(request))
            tpl = "rrhh/paso0.html"
        return render(request, tpl, ctx)


admin.site.register(Person, person_admin)

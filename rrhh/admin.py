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
    fields = ('nombre', ('cedula', 'salario'), 'fecha_ingreso',
        ('moneda', 'tc'), 'cuenta')
    actions = ['planilla_dia', 'planilla_mes']

    class rango_fecha(forms.Form):
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
        fecha_inicial = forms.DateField(widget=widgets.AdminDateWidget())
        fecha_final = forms.DateField(widget=widgets.AdminDateWidget())

    class config_mes(forms.Form):
        MESES = (
        ("ENERO", "ENERO"),
        ("FEBRERO", "FEBRERO"),
        ("MARZO", "MARZO"),
        ("ABRIL", "ABRIL"),
        ("MAYO", "MAYO"),
        ("JUNIO", "JUNIO"),
        ("JULIO", "JULIO"),
        ("AGOSTO", "AGOSTO"),
        ("SEPTIEMBRE", "SEPTIEMBRE"),
        ("OCTUBRE", "OCTUBRE"),
        ("NOVIEMBRE", "NOVIEMBRE"),
        ("DICIEMBRE", "DICIEMBRE"),
        )
        QUINSENAS = (
        ("PRIMERA", "PRIMERA"),
        ("SEGUNDA", "SEGUNDA"),
        ("AMBAS", "AMBAS"),
        )
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
        mes = forms.ChoiceField(choices=MESES)
        quinsena = forms.ChoiceField(choices=QUINSENAS)

    def planilla_dia(self, request, queryset):
        message = ""
        form = None
        data = {}
        data['header_tittle'] = 'Por Favor complete todos los campos'
        data['explanation'] = 'Las Siguientes personas estan incluidas en esta planilla:'
        data['action'] = 'planilla_dia'
        if 'calcular' in request.POST:
            form = self.rango_fecha(request.POST)
            if form.is_valid():
                fecha_inicial = datetime.strptime(request.POST.get('fecha_inicial', ''), "%d/%m/%Y")
                fecha_final = datetime.strptime(request.POST.get('fecha_final', ''), "%d/%m/%Y")
                data['dias'] = (fecha_final - fecha_inicial).days + 1
                data['queryset'] = [x.pago_dias(data['dias']) for x in queryset]
                data['header_tittle'] = 'Detalle de Pago de Planilla del periodo entre %s y %s' % (str(fecha_inicial), str(fecha_final))
                data['explanation'] = 'Se requerira Autorizacion de Gerencia para aplicar las Notas de Credito.'
                data.update(csrf(request))
                return render_to_response('rrhh/pago_dias.html', data, RequestContext(request))

        if not form:
            form = self.rango_fecha(
                initial={
                    '_selected_action': request.POST.getlist(
                        admin.ACTION_CHECKBOX_NAME)})
        data['queryset'] = queryset
        data['form'] = form
        data.update(csrf(request))
        self.message_user(request, message)
        return render_to_response('rrhh/pago_dias.html', data, RequestContext(request))
    planilla_dia.short_description = "Generar planilla de corte por Dia"

    def planilla_mes(self, request, queryset):
        message = ""
        form = None
        data = {}
        data['header_tittle'] = 'Por Favor complete todos los campos'
        data['explanation'] = 'Las Siguientes personas estan incluidas en esta planilla:'
        data['action'] = 'planilla_mes'
        if 'calcular' in request.POST:
            form = self.config_mes(request.POST)
            if form.is_valid():
                mes = request.POST.get('mes', '')
                quinsena = request.POST.get('quinsena', '')
                if quinsena == "AMBAS":
                    data['header_tittle'] = 'Detalle de Pago de Planilla del mes de %s' % (mes)
                else:
                    data['header_tittle'] = 'Detalle de Pago de Planilla del mes de %s %s quinsena' % (mes, quinsena)
                data['mes'] = mes
                data['queryset'] = [x.pago_mes(quinsena, mes) for x in queryset]
                data['explanation'] = 'Se requerira Autorizacion de Gerencia para aplicar las Notas de Credito.'
                data.update(csrf(request))
                return render_to_response('rrhh/pago_mes.html', data, RequestContext(request))

        if not form:
            form = self.config_mes(
                initial={
                    '_selected_action': request.POST.getlist(
                        admin.ACTION_CHECKBOX_NAME)})
        data['queryset'] = queryset
        data['form'] = form
        data.update(csrf(request))
        self.message_user(request, message)
        return render_to_response('rrhh/pago_mes.html', data, RequestContext(request))
    planilla_dia.short_description = "Generar planilla de corte por Dia"

admin.site.register(Person, person_admin)

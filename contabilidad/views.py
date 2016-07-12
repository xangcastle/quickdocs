from django.views.generic.base import TemplateView
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
import operator
from django.db.models import Q
from django.http.response import HttpResponse


class index(TemplateView):
    template_name = "contabilidad/base.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['izquierda'] = Cuenta.izquierda.all()
        context['derecha'] = Cuenta.derecha.all()
        return super(index, self).render_to_response(context)


class comprobantes(TemplateView):
    template_name = "contabilidad/comprobantes.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        if request.GET.get('nuevo', '') == "True":
            context['nuevo'] = True
        else:
            if request.GET.get('id', None):
                print("vamos")
                context['comprobante'] = Comprobante.objects.get(
                    id=request.GET.get('id', None))
        return super(comprobantes, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        pk = request.POST.get('id', None)
        if not pk or pk == "":
            c = Comprobante(numero='1',
                concepto=request.POST.get('concepto', ''),
                fecha=datetime.strptime(
                    request.POST.get('fecha', ''), '%m/%d/%Y').date(),
                tipo="CD")
            c.save()
            for i in range(0, len(request.POST.getlist('mov-code', ''))):
                m = Movimiento(comprobante=c,
                    cuenta=Cuenta.objects.get(
                        code=request.POST.getlist('mov-code', '')[i]),
                    debe=request.POST.getlist('mov-debe', '')[i],
                    haber=request.POST.getlist('mov-haber', '')[i])
                m.save()
        context['mensaje'] = "comprobante grabado con exito"
        return super(comprobantes, self).render_to_response(context)


@csrf_exempt
def datos_comprobante(request):
    if request.is_ajax:
        model = Comprobante
        result = []
        pk = request.POST.get('id', None)
        obj = model.objects.get(id=pk)
        if obj:
            try:
                result = obj.to_json()
            except:
                result = model_to_dict(obj)
            data = json.dumps(result)
    else:
        data = 'fail'
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def tableComprobante(request):
    obj = Comprobante
    try:
        objs = obj.objects.all()
    except:
        pass
    table = {"data": []}
    for o in objs:
        table['data'].append(model_to_dict(o))
    data = json.dumps(table, cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


def querie(sentence):
    predicates = []
    for word in sentence.split(" "):
        predicates.append(('name__icontains', word))
    predicates.append(('code__istartswith', sentence))
    return [Q(x) for x in predicates]


def autocomplete_entidad(instance, request):
    if request.is_ajax:
        model = type(instance)
        result = []
        term = request.GET.get('term', None)
        words = querie(term)
        qs = model.objects.filter(reduce(operator.or_, words))
        for obj in qs:
            obj_json = {}
            obj_json['label'] = obj.name
            obj_json['value'] = obj.name
            obj_json['obj'] = model_to_dict(obj)
            result.append(obj_json)
        data = json.dumps(result)
    else:
        data = 'fail'
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def autocomplete_cuenta(request):
    if request.is_ajax:
        model = Cuenta
        result = []
        term = request.GET.get('term', None)
        words = querie(term)
        qs = model.objects.filter(reduce(operator.or_, words))
        queryset = []
        for q in qs:
            if q.is_operativa():
                queryset.append(q)
        for obj in queryset:
            obj_json = {}
            obj_json['label'] = obj.name
            obj_json['value'] = obj.name
            obj_json['obj'] = model_to_dict(obj)
            result.append(obj_json)
        data = json.dumps(result)
    else:
        data = 'fail'
    return HttpResponse(data, content_type='application/json')
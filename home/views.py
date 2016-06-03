from django.views.generic.base import TemplateView
from django.http.response import HttpResponse
from quickdoc.models import *
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json


class index(TemplateView):
    template_name = "home/base.html"


class expediente(TemplateView):
    template_name = "home/expediente.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        pk = request.GET.get('id', None)
        if pk:
            context['expediente'] = Expediente.objects.get(id=pk)
        return super(expediente, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        pk = request.POST.get('buscador', None)
        if pk:
            context['expediente'] = Expediente.objects.get(id=pk)
        return super(expediente, self).render_to_response(context)


@csrf_exempt
def datos_expediente(request):
    if request.is_ajax:
        model = Expediente
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
def tableExpediente(request):
    obj = Expediente
    try:
        objs = obj.objects.all()
    except:
        pass
    table = {"data": []}
    for o in objs:
        table['data'].append(model_to_dict(o))
    data = json.dumps(table)
    return HttpResponse(data, content_type='application/json')
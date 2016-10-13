from django.shortcuts import render_to_response
from django.template import RequestContext
import os
from .models import *
import json
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def get_ruta(paquete):
    carpeta_madre = paquete.expediente.codigo
    ruta = os.path.join('EXPEDIENTES', carpeta_madre)
    return ruta


def generar_ruta_comprobante(paquete, filename):
        extension = os.path.splitext(filename)[1][1:]
        nombre = paquete.indice.indice
        nombre_archivo = '{}.{}'.format(nombre, extension)
        ruta = os.path.join(get_ruta(paquete), nombre_archivo)
        try:
            os.remove(os.path.join(settings.MEDIA_ROOT, ruta))
        except:
            pass
        return ruta


def cargar_comprobante(paquete, path):
    p = Documento.objects.get(id=paquete.id)
    p.documento.name = generar_ruta_comprobante(paquete, 'archivo.pdf')
    p.save()
    ruta = os.path.join(settings.MEDIA_ROOT, get_ruta(p))
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    os.rename(path, os.path.join(settings.MEDIA_ROOT,
    p.documento.path))
    return p


@csrf_exempt
def cargar_pod(request):
    data = {'mensaje': "carga correcta"}
    c = request.GET.get('code', '00000000000')
    p = Documento.objects.get(code=c)
    if p:
        path = settings.MEDIA_ROOT + str(
            request.GET.get('path', '')).replace('media/', '')
        path = path.replace('//', '/')
        p = cargar_comprobante(p, path)
        p.save()
    else:
        data['mensaje'] = "carga_incorrecta"
    return HttpResponse(json.dumps(data), content_type='application/json')


def carga_manual(request, id):
    i = Indexacion.objects.get(id=id)
    base = i.url()
    archivos = i.pendientes()[:30]
    data = []
    for a in archivos:
        p = os.path.join(base, a)
        data.append(p)
    return render_to_response("digitalizacion/carga_manual.html",
        {'archivos': data, 'id': i.id},
        context_instance=RequestContext(request))


def autocomplete_pod(request):
    if request.is_ajax:
        model = Documento
        result = []
        indexacion = Indexacion.objects.get(id=int(request.GET.get('id', '')))
        code = indexacion.cliente.codigo + str(indexacion.numero) + \
        request.GET.get('term', '')
        qs = model.objects.filter(code__istartswith=code)
        for obj in qs:
            obj_json = {}
            obj_json['label'] = str('%s | %s' % (
                obj.expediente.nombre.encode('ascii', 'ignore'),
                obj.indice.indice))
            obj_json['value'] = str(obj.code)
            result.append(obj_json)
        data = json.dumps(result)
    else:
        data = 'fail'
    return HttpResponse(data, content_type='application/json')

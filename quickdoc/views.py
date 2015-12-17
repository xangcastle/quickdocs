from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='/admin/login/')
def consulta(request):
    context = RequestContext(request)
    indice = Indice.superiores.all().order_by('indice')
    cuentas = Expediente.objects.all()[0].cuentas()
    info = Expediente.objects.all()[0].informacion_general().order_by('indice')
    data = {'indice': indice, 'cuentas': cuentas, 'info': info}
    template_name = "quickdocs/base.html"
    return render_to_response(template_name, data, context_instance=context)


def ver_expediente(request, id):
    ctx = {'expediente': Expediente.objects.get(id=id)}
    return render_to_response("quickdocs/base.html", ctx,
        context_instance=RequestContext(request))

from django.views.generic.base import TemplateView
from quickdoc.models import *


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
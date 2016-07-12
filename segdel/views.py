from django.views.generic.base import TemplateView
from .models import *


class index(TemplateView):
    template_name = "segdel/base.html"

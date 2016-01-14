from django.db import models
import os
from django.conf import settings
import shutil


def get_media_url(model, filename):
    clase = model.__class__.__name__
    code = str(model.id)
    return '%s/%s/%s' % (clase, code, filename)


class Empleado(models.Model):
    idempleado = models.PositiveIntegerField(null=True, blank=True,
        verbose_name="codigo de empleado")
    nombre = models.CharField(max_length=120, null=True, blank=True)
    cedula = models.CharField(max_length=14, null=True, blank=True)
    gerencia = models.CharField(max_length=65, null=True, blank=True)
    localidad = models.CharField(max_length=65, null=True, blank=True)
    ecuenta = models.FileField(upload_to=get_media_url, null=True,
        blank=True, verbose_name="estado de cuenta")

    def __unicode__(self):
        return self.nombre

    def link_ecuenta(self):
        if self.ecuenta:
            return '<a href="/media/%s" target="blank" onclick="return showAddAnotherPopup(this);">%s</a>' % (self.ecuenta,
                'ver estado de cuenta')
        else:
            return ''

    def export_path(self):
        path = os.path.join(settings.MEDIA_ROOT, 'TEMP')
        if not os.path.exists(path):
                os.makedirs(path)
        return path

    def get_name(self):
        return str(self.idempleado)

    def exportar_ecuenta(self, name=None):
        if self.ecuenta:
            o = self.ecuenta.path
            if name:
                d = os.path.join(self.export_path(), name)
            else:
                d = os.path.join(self.export_path(), self.get_name())
            shutil.copy(o, d)

    link_ecuenta.short_description = ''
    link_ecuenta.allow_tags = True


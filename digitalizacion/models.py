from django.db import models
import os
from django.conf import settings
import shutil
import pyPdf
import string
import random
from quickdoc.models import *
from multifilefield.models import MultiFileField


def get_media_url(model, filename):
    clase = model.__class__.__name__
    code = str(model.id)
    return '%s/%s/%s' % (clase, code, filename)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def limpiar_caracteres(texto):
    for l in texto:
        if l not in ['A', 'B', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J''K', 'L',
            'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            ' ']:
            texto = texto.replace(l, '')
    return texto


def limpiar_espacios(texto):
    texto = texto.replace(' ', '')
    return texto


def eliminar_letras(texto):
    for l in texto:
        if l not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']:
            texto = texto.replace(l, '')
    return texto


def extract_content(pdf):
    content = ""
    content += pdf.getPage(0).extractText() + "\n"
    content = content.encode("ascii", "ignore")
    content = " ".join(content.replace("\xa0", " ").strip().split())
    return content


def extract_code(content):
    code = []
    todo = eliminar_letras(content).split(" ")
    for n in todo:
        if len(n) >= 15:
            code.append(n)
    return code


def comprobacion(code):
    p = None
    queryset = Documento.objects.filter(code=code)
    if queryset.count() > 0:
        p = queryset[0]
    if p:
        return p
    else:
        return None


def cargar_archivo(documento, path):
    if documento:
        documento.documento.name = get_media_url(documento, 'archivo.pdf')
        documento.save()
        ruta = documento.documento.path
        carpeta = ruta.replace(os.path.basename(ruta), '')
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        os.rename(path, os.path.join(settings.MEDIA_ROOT,
        documento.documento.path))


def descomponer(path):
    data = {}
    data['carpeta'] = path.replace(os.path.basename(path), '')
    data['archivo'] = os.path.splitext(os.path.basename(path))[0][0:]
    data['extension'] = os.path.splitext(path)[1][1:]
    return data


def make_ocr(path):
    nr = os.path.join(descomponer(path)['carpeta'],
        '{}.{}'.format(descomponer(path)['archivo'] + '_ocr',
            descomponer(path)['extension']))
    os.system("pypdfocr " + path)
    os.remove(path)
    return nr


def save_content(path, content):
    f = open(os.path.join
    (descomponer(path)['carpeta'], '{}.{}'.format(
        descomponer(path)['archivo'] + '_txt', 'txt')), 'w')
    f.write(content)
    f.close()


def indexar(path, indexacion):
    pdf = None
    if indexacion.make_ocr:
        path = make_ocr(path)
    pdf = pyPdf.PdfFileReader(file(path, "r"))
    content = extract_content(pdf)
    code = extract_code(content)
    if len(code) > 0:
        for c in code:
            d = comprobacion(c)
        cargar_archivo(d, path)


def preparar_carpeta(path):
    comand = "cd %s && mkdir tm && pdftk *.pdf cat output tm/1.pdf && rm *.pdf"
    comand += " && mv tm/1.pdf 1.pdf && pdftk 1.pdf burst"
    comand += " && rm doc_data.txt 1.pdf && rm -rf tm"
    comand = comand % (path)
    try:
        os.system(comand)
        return True
    except:
        return False


def indexar_carpeta(indexacion):
    archivos = sorted(os.listdir(path))
    for a in archivos:
        if a[-3:] == 'pdf':
            path = os.path.join(indexacion.path(), a)
            indexar(path, indexacion)
        #os.system("rm -rf %s" % path)


def recoger_archivos(fecha):
    o = '/home/abel/workspace/deltacopiers/deltacopiers/media'
    d = o + '/TEMP/' + id_generator()
    comand = "mkdir %s && mv %s/*.pdf %s" % (d, o, d)
    try:
        os.system(comand)
    except:
        pass
    indexar_carpeta(d, fecha)


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


def get_path(indexacion, filename):
    return os.path.join(indexacion.path(), filename)


class Indexacion(models.Model):
    fecha = models.DateField(auto_now_add=True, null=True)
    archivos = MultiFileField(upload_to=get_path, null=True, blank=True)
    cliente = models.ForeignKey(Expediente, null=True, blank=True)
    producto = models.ForeignKey(Producto, null=True, blank=True)
    numero = models.CharField(max_length=25, null=True, blank=True)
    carpeta = models.CharField(max_length=8, null=True, blank=True)
    make_ocr = models.BooleanField(default=False, verbose_name="hacer ocr")

    def path(self):
        return os.path.join(settings.MEDIA_ROOT, 'Indexacion', self.carpeta)

    def url(self):
        if not self.carpeta:
            self.carpeta = id_generator()
        return os.path.join('/media', 'Indexacion', self.carpeta)

    def resumen_por_ciclo(self):
        data = []
        cls = self.comprobantes().distinct('ciclo').order_by('ciclo')
        for c in cls:
            data.append((c.ciclo, self.comprobantes(
                ).filter(ciclo=c.ciclo).count()))
        return data

    def pendientes(self):
        archivos = []
        path = self.path()
        if os.path.exists(path):
            archivos = sorted(os.listdir(path))
        return archivos

    def carga_manual(self):
        data = self.pendientes()
        return '<a href="/digitalizacion/carga_manual/%s/" target="blank">%s comprobantes</a>' % (self.id ,len(data))
    carga_manual.allow_tags = True
    carga_manual.short_description = "Archivos Pendientes"

    class Meta:
        verbose_name_plural = "carga de imagenes masiva"
        verbose_name = "archivos pdf"

    def __unicode__(self):
        return str(self.fecha) + " - " + str(self.carpeta)

    def save(self, *args, **kwargs):
        if not self.carpeta:
            self.carpeta = id_generator()
        super(Indexacion, self).save()
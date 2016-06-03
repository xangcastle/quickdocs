from django.db import models
from django.db.models import Max
from django.forms.models import model_to_dict


def get_media_url(model, filename):
    clase = model.__class__.__name__
    code = str(model.id)
    return '%s/%s/%s' % (clase, code, filename)


def get_by_code(instance, code):
    model = type(instance)
    try:
        return model.objects.get(code=code)
    except:
        return instance


def get_by_name(instance, name):
    model = type(instance)
    try:
        return model.objects.get(name=name)
    except:
        return instance


def get_or_create_entidad(instance, name):
    model = type(instance)
    o, created = model.objects.get_or_create(name=name)
    o.save()
    return o


def get_code(entidad):
        model = type(entidad)
        code = '1'
        sets = model.objects.filter(code__isnull=False)
        if sets:
            maxi = str(sets.aggregate(Max('code'))['code__max'])
            if maxi:
                consecutivo = list(range(1, int(maxi)))
                ocupados = list(sets.values_list('code',
                flat=True))
                n = 0
                for l in ocupados:
                    ocupados[n] = int(str(l))
                    n += 1
                disponibles = list(set(consecutivo) - set(ocupados))
                if len(disponibles) > 0:
                    code = min(disponibles)
                else:
                    code = max(ocupados) + 1
        return str(code).zfill(4)


class base(models.Model):

    def __iter__(self):
        for field_name in self._meta.get_all_field_names():
            try:
                value = getattr(self, field_name)
            except:
                value = None
            yield (field_name, value)

    class Meta:
        abstract = True


class base_entidad(base):
    code = models.CharField(max_length=25, null=True, blank=True,
        verbose_name="codigo")
    name = models.CharField(max_length=100, verbose_name="nombre")

    class Meta:
        abstract = True


class Entidad(base_entidad):
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        if self.code and self.name:
            return str(self.code) + " " + self.name
        elif self.name:
            return self.name
        elif self.code:
            return str(self.code)
        else:
            return ''

    @staticmethod
    def autocomplete_search_fields():
        return ("code__iexact", "name__icontains",)

    def save(self, *args, **kwargs):
        if self.code is None or self.code == '':
            self.code = get_code(self)
        super(Entidad, self).save()

    class Meta:
        abstract = True
        ordering = ['code']


TIPOS_PERSONAS = (
    ('NATURAL', 'NATURAL'),
    ('JURIDICO', 'JURIDICO'),
    )


class base_expediente(models.Model):
    codigo = models.CharField(max_length=10, null=True,
        verbose_name="Codigo del Cliente")
    identificacion = models.CharField(max_length=30, null=True,
        verbose_name="No de Identificacion")
    nombre = models.CharField(max_length=150, null=True,
        verbose_name="Nombre Completo")
    tipo = models.CharField(max_length=25, null=True,
        verbose_name="Tipo Documento", choices=TIPOS_PERSONAS)

    @staticmethod
    def autocomplete_search_fields():
        return ("codigo__iexact", "identificacion__iexact",
            "nombre__icontains",)

    class Meta:
        abstract = True


class Expediente(base_expediente):

    def __unicode__(self):
        return ' '.join([self.codigo, self.nombre])

    def documentos(self):
        return Documento.objects.filter(expediente=self)

    def ver_expediente(self):
        return '<a href="/home/expediente/?id=%s" target="blank">Ver expediente</a>' % (self.id)
    ver_expediente.allow_tags = True

    def productos(self):
        return producto_cliente.objects.filter(cliente=self)

    def render_data(self):
        data = []
        if self.documentos():
            secciones = self.documentos().order_by(
                'producto').distinct('producto')
            for s in secciones:
                seccion = {'name': s.producto.name, 'productos': []}
                productos = self.documentos().filter(
                    producto=s.producto).order_by('numero').distinct('numero')
                for p in productos:
                    producto = {'numero': p.numero, 'documentos': []}
                    documentos = self.documentos().filter(producto=p.producto,
                        numero=p.numero)
                    for d in documentos:
                        documento = {'indice': d.indice.indice,
                            'nombre': d.indice.name}
                        if d.documento:
                            documento['con_imagen'] = True
                            documento['url'] = d.documento.url
                        else:
                            documento['con_imagen'] = False
                            documento['url'] = "#"
                        producto['documentos'].append(documento)
                    seccion['productos'].append(producto)
                data.append(seccion)
        return data

    def to_json(self):
        obj = model_to_dict(self)
        obj['indice'] = self.render_data()
        return obj

    def indices(self):
        indices = []
        if self.productos():
            for p in self.productos():
                for i in p.producto.indices.all():
                    d = {'indice': i.code, 'descripcion': i.name,
                        'numero': p.numero, 'code': self.codigo,
                        'barra': str(self.codigo) + str(p.numero) + str(i.code),
                        'indice_id': i.id}
                    indices.append(d)
        return indices

    def generar_documentos(self):
        if self.productos():
            for p in self.productos():
                for i in p.producto.indices.all():
                    d, created = Documento.objects.get_or_create(
                    code=str(self.codigo) + str(p.numero) + str(i.code),
                    indice=i,
                    expediente=self, producto=p.producto)
                    if p.numero:
                        d.numero = p.numero
                    d.save()

    class Meta:
        verbose_name = "expediente"
        verbose_name_plural = "consulta de expedientes"


class Indice(Entidad):
    indice = models.CharField(max_length=6)
    tipo = models.CharField(max_length=25, null=True,
        verbose_name="Tipo Documento", choices=TIPOS_PERSONAS)

    objects = models.Manager()

    def __unicode__(self):
        return "%s %s %s" % (self.indice, self.name, self.tipo)

    class Meta:
        ordering = ('indice',)
        unique_together = ("indice", "tipo")
        verbose_name = "indice"
        verbose_name_plural = "configuracion de secciones"

    def sub_indices(self):
        return Indice.objects.filter(indice_superior=self)


class base_documento(models.Model):
    numero = models.CharField(max_length=125, null=True)
    expediente = models.ForeignKey(Expediente, null=True)
    documento = models.FileField(upload_to=get_media_url, null=True, blank=True)
    code = models.CharField(max_length=125, null=True)

    class Meta:
        abstract = True


class Documento(base_documento):
    indice = models.ForeignKey(Indice, null=True)
    producto = models.ForeignKey('Producto', null=True)

    def get_code(self):
        code = self.expediente.codigo + self.producto.numero \
        + self.indice.indice
        return code

    def save(self, *args, **kwars):
        if not self.code:
            self.code = self.get_code()
        super(Documento, self).save()


class Producto(Entidad):

    indices = models.ManyToManyField(Indice, null=True,
        verbose_name="documentacion requerida")

    def __unicode__(self):
        return " ".join([self.code, self.name])

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "productos y servicios"


class producto_cliente(models.Model):
    cliente = models.ForeignKey(Expediente)
    producto = models.ForeignKey(Producto)
    numero = models.CharField(max_length=60, null=True, blank=True)

    def __unicode__(self):
        return " ".join([self.producto.name, self.numero])

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos del cliente"


class Importacion(base_expediente):
    producto = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return ' '.join([self.producto, self.numero])

    def get_expediente(self):
        e, created = Expediente.objects.get_or_create(codigo=self.codigo)
        e.identificacion = self.identificacion
        e.nombre = self.nombre
        e.tipo = self.tipo
        e.save()
        return e

    def get_producto(self):
        return get_or_create_entidad(Producto(), self.producto)

    def integrar(self):
        cliente = self.get_expediente()
        producto = self.get_producto()
        if self.numero:
            pc, created = producto_cliente.objects.get_or_create(
                cliente=cliente, producto=producto, numero=self.numero)
        self.delete()

    class Meta:
        verbose_name = "registro"
        verbose_name_plural = "importacion de datos"
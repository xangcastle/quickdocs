from django.db import models


def get_media_url(model, filename):
    clase = model.__class__.__name__
    code = str(model.id)
    return '%s/%s/%s' % (clase, code, filename)


class Expediente(models.Model):
    codigo = models.CharField(max_length=10, null=True,
        verbose_name="Codigo del Cliente")
    identificacion = models.CharField(max_length=30, null=True,
        verbose_name="No de Identificacion")
    nombre = models.CharField(max_length=150, null=True,
        verbose_name="Nombre Completo")
    tipodoc = models.CharField(max_length=50, null=True,
        verbose_name="Tipo Documento")

    def documentos(self):
        return Documento.objects.filter(expediente=self)

    def informacion_general(self):
        indice_info = Indice.objects.filter(indice__startswith="A.")
        return self.documentos().filter(indice__in=indice_info)

    def cuentas(self):
        cuentas = []
        indice_cuentas = Indice.objects.filter(indice__startswith="B.")
        cs = self.documentos().filter(indice__in=indice_cuentas).order_by(
            'numero').distinct('numero')
        for c in cs:
            cuenta = {}
            cuenta['numero'] = c.numero
            cuenta['documentos'] = self.documentos().filter(
                numero=c.numero).order_by('indice')
            cuentas.append(cuenta)
        return cuentas

    def depositos(self):
        cuentas = []
        indice_cuentas = Indice.objects.filter(indice__startswith="C.")
        cs = self.documentos().filter(indice__in=indice_cuentas).order_by(
            'numero').distinct('numero')
        for c in cs:
            cuenta = {}
            cuenta['numero'] = c.numero
            cuenta['documentos'] = self.documentos().filter(
                numero=c.numero).order_by('indice')
            cuentas.append(cuenta)
        return cuentas

    def tarjetas(self):
        cuentas = []
        indice_cuentas = Indice.objects.filter(indice__startswith="D.")
        cs = self.documentos().filter(indice__in=indice_cuentas).order_by(
            'numero').distinct('numero')
        for c in cs:
            cuenta = {}
            cuenta['numero'] = c.numero
            cuenta['documentos'] = self.documentos().filter(
                numero=c.numero).order_by('indice')
            cuentas.append(cuenta)
        return cuentas

    def ver_expediente(self):
        return '<a href="/quickdoc/expediente/%s/" target="blank">Ver expediente</a>' % (self.id)
    ver_expediente.allow_tags = True


class superiores(models.Manager):
    def get_queryset(self):
        return super(superiores, self).get_queryset().filter(
            indice_superior=None)


class intermedios(models.Manager):
    def get_queryset(self):
        return Indice.objects.filter(
            indice_superior__in=Indice.superiores.all())


class inferiores(models.Manager):
    def get_queryset(self):
        return Indice.objects.filter(
                indice_superior__in=Indice.intermedios.all())


class naturales(models.Manager):

    def get_queryset(self):
        return super(naturales, self).get_queryset().filter(
            tipo_expediente='NATURAL')


class juridicos(models.Manager):

    def get_queryset(self):
        return super(juridicos, self).get_queryset().filter(
            tipo_expediente='JURIDICO')


class Indice(models.Model):
    indice = models.CharField(max_length=6)
    descripcion = models.CharField(max_length=200)
    indice_superior = models.ForeignKey('self', null=True,
        related_name="relacion_indice_superior", blank=True)
    TIPOS_EXPEDIENTE = (
            ('NATURAL', 'NATURAL'),
            ('JURIDICO', 'JURIDICO')
        )
    tipo_expediente = models.CharField(max_length=25, null=True, blank=True,
        choices=TIPOS_EXPEDIENTE)
    objects = models.Manager()
    superiores = superiores()
    intermedios = intermedios()
    inferiores = inferiores()

    def __unicode__(self):
        return "%s %s" % (self.indice, self.descripcion)

    class Meta:
        ordering = ('indice',)

    def sub_indices(self):
        return Indice.objects.filter(indice_superior=self)


class indice_superior(Indice):
    objects = models.Manager()
    objects = superiores()

    class Meta:
        proxy = True


class indice_intermedio(Indice):
    objects = models.Manager()
    objects = intermedios()

    class Meta:
        proxy = True


class indice_inferior(Indice):
    objects = models.Manager()
    objects = inferiores()

    class Meta:
        proxy = True


class expediente_natural(Indice):
    objects = models.Manager()
    objects = naturales()

    class Meta:
        proxy = True


class expediente_juridico(Indice):
    objects = models.Manager()
    objects = juridicos()

    class Meta:
        proxy = True


class base_documento(models.Model):
    numero = models.CharField(max_length=25, null=True)
    expediente = models.ForeignKey(Expediente, null=True)
    documento = models.FileField(upload_to=get_media_url, null=True, blank=True)

    class Meta:
        abstract = True


class Documento(base_documento):
    indice = models.ForeignKey(Indice, null=True)


class documento_natural(base_documento):
    indice = models.ForeignKey(expediente_natural, null=True)

    class Meta:
        managed = False
        db_table = 'quickdoc_documento'


class documento_juridico(base_documento):
    indice = models.ForeignKey(expediente_juridico, null=True)

    class Meta:
        managed = False
        db_table = 'quickdoc_documento'
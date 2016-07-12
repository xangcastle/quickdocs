from django.db import models
from datetime import datetime
from django.db.models import Sum, Q


RUBROS = (
('ACTIVO', 'ACTIVO'),
('PASIVO', 'PASIVO'),
('CAPITAL', 'CAPITAL'),
('INGRESO', 'INGRESO'),
('EGRESO', 'EGRESO'),
)

TIPOS_CUENTA = (
('RUBRO', 'RUBRO'),
('GRUPO', 'GRUPO'),
('MAYOR', 'MAYOR'),
('SUB-CTA', 'SUB-CTA'),
('AUXILIAR', 'AUXILIAR'),
)


class BalanzaIzquierda(models.Manager):

    def get_queryset(self):
        queryset = super(BalanzaIzquierda, self).get_queryset().filter(
            Q(code__istartswith='1'))
        data = []
        for obj in queryset:
            if not obj.is_operativa():
                data.append(obj)
        return data


class BalanzaDerecha(models.Manager):

    def get_queryset(self):
        queryset = super(BalanzaDerecha, self).get_queryset().filter(
            Q(code__istartswith='2') |
            Q(code__istartswith='3'))
        data = []
        for obj in queryset:
            if not obj.is_operativa():
                data.append(obj)
        return data


class Cuenta(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=125)
    parent = models.ForeignKey('self', null=True, blank=True)
    clase = models.CharField(max_length=15, null=True, choices=RUBROS)
    tipo = models.CharField(max_length=15, null=True, choices=TIPOS_CUENTA)
    active = models.BooleanField(default=True)

    objects = models.Manager()
    izquierda = BalanzaIzquierda()
    derecha = BalanzaDerecha()

    def __unicode__(self):
        return " ".join([self.code, self.name])

    def periodo_actual(self):
        p = None
        p = Periodo.objects.filter(cerrado=False).order_by('-ano', '-mes')
        if len(p) > 0:
            return p[0]
        else:
            p, created = Periodo.objects.get_or_create(
                ano=datetime.now().year, mes=datetime.now().month)
            if created:
                p.aperturar_saldos()
            return p

    def movimientos(self, periodo=None):
        if not periodo:
            periodo = self.periodo_actual()
        return Movimiento.objects.filter(cuenta=self,
            comprobante__in=Comprobante.objects.filter(
                periodo=periodo))

    def total_debitos(self, periodo=None):
        if not periodo:
            periodo = self.periodo_actual()
        if self.is_operativa():
            total = self.movimientos(periodo).aggregate(
                Sum('debe'))["debe__sum"]
            if total:
                return total
            else:
                return 0.0
        else:
            return 0.00

    def total_creditos(self, periodo=None):
        if not periodo:
            periodo = self.periodo_actual()
        if self.is_operativa():
            total = self.movimientos(periodo).aggregate(
                Sum('haber'))["haber__sum"]
            if total:
                return total
            else:
                return 0.0
        else:
            return 0.00

    def sub_cuentas(self):
        return Cuenta.objects.filter(code__istartswith=self.code)

    def saldo(self, periodo=None):
        if not periodo:
            periodo = self.periodo_actual()
        if self.is_operativa():
            return CuentaPeriodo.objects.get(periodo=periodo,
                cuenta=self).saldo_inicial +\
                self.total_creditos(periodo) - \
                self.total_debitos(periodo)
        else:
            total = 0.0
            for c in self.childs():
                total += c.saldo()
            return total

    def render_parent(self):
        if self.parent:
            return self.parent.id
        else:
            return ""

    def childs(self):
        return Cuenta.objects.filter(parent=self)

    def get_class(self):
        if self.parent:
            if self.childs():
                return "parent"
            else:
                return "child"
        else:
            return "parent"

    def is_operativa(self):
        if self.get_class() == "parent":
            return False
        else:
            return True

    def get_parent(self):
        if len(self.code) == 1:#1
            return None #rubro
        elif len(self.code) == 2: #11
            return Cuenta.objects.get(code=self.code[:1]) #grupo
        elif len(self.code) == 4: #1111
            return Cuenta.objects.get(code=self.code[:2]) #mayor
        elif len(self.code) == 6: #1111-01
            return Cuenta.objects.get(code=self.code[:4]) #sub cuenta
        elif len(self.code) == 9: #1111-01-001
            return Cuenta.objects.get(code=self.code[:6]) #auxiliar

    class Meta:
        ordering = ['code', ]

    def save(self, *args, **kwargs):
        if not self.parent:
            self.parent = self.get_parent()
        super(Cuenta, self).save()


def get_periodo(fecha):
    return Periodo.objects.get_or_create(ano=fecha.year, mes=fecha.month)[0]


class Periodo(models.Model):
    ano = models.PositiveIntegerField()
    mes = models.PositiveIntegerField()
    cerrado = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.mes) + '-' + str(self.ano)

    def aperturar_saldos(self):
        for c in Cuenta.objects.all():
            if c.is_operativa():
                cp, created = CuentaPeriodo.objects.get_or_create(cuenta=c,
                    periodo=self)

    def cuentas(self):
        return CuentaPeriodo.objects.filter(periodo=self)

    def cerrar(self):
        for c in self.cuentas():
            c.saldo_final = c.cuenta.saldo(periodo=self)
            c.save()
        self.cerrado = True
        self.save()


class CuentaPeriodo(models.Model):
    cuenta = models.ForeignKey(Cuenta)
    periodo = models.ForeignKey(Periodo)
    saldo_inicial = models.FloatField(default=0.00)
    saldo_final = models.FloatField(default=0.00)


class Comprobante(models.Model):
    TIPOS_DOCUMENTOS = (
    ('CK', 'Cheque'),
    ('CD', 'Comprobante de Diario'),
    ('AJ', 'Documento de Ajuste'),
        )
    fecha = models.DateTimeField()
    numero = models.PositiveIntegerField()
    tipo = models.CharField(max_length=2, choices=TIPOS_DOCUMENTOS,
        default='CD')
    periodo = models.ForeignKey(Periodo)
    concepto = models.TextField(max_length=400)

    def __unicode__(self):
        return ' '.join([self.tipo, str(self.numero)])

    def movimientos(self):
        return Movimiento.objects.filter(comprobante=self)

    def save(self, *args, **kwargs):
        if not self.fecha:
            self.fecha = datetime.now()
        self.periodo = get_periodo(self.fecha)
        super(Comprobante, self).save()


class Movimiento(models.Model):
    comprobante = models.ForeignKey(Comprobante)
    cuenta = models.ForeignKey(Cuenta)
    debe = models.FloatField(default=0.00)
    haber = models.FloatField(default=0.00)

    def tipo(self):
        if self.debe > self.haber:
            return "debito"
        else:
            return "credito"

    def total_movimiento(self):
        return abs(self.debe - self.haber)

    def __unicode__(self):
        return "%s a la cuenta %s - %s por %s" % \
        (self.tipo(), self.cuenta.code,
            self.cuenta.name, self.total_movimiento())
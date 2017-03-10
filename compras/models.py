from django.db import models
from django.contrib.auth.models import User


FORMAS_PAGO = (
    ('NC', "NOTA DE CREDITO"),
    ('CK', "CHEQUE"),
    ('TFI', "TRANSFERENCIA INTERNACIONAL"),
    ('TFCI', "TRANSFERENCIA CUENTA INTEGRA"),
)


TIPOS_PROVEEDOR = (
    ('PE', "PERMANENTE"),
    ('OC', "OCACIONAL"),
)



# Valores de la Evaluacion

IMPORTANCIA = ((15, "SI"), (0, "NO"))
COMPLEJIDAD = ((10, "ALTA"), (0, "BAJA"))
REEMPLAZO = ((10, "ALTA COMPLEJIDAD"), (0, "COMPLEJIDAD ACEPTABLE"))
CREDITO = ((10, "B, C, D o D"), (0, "Excelentes (A), No encontrado/consultado, Ninguna"))
ANUAL = ((10, "Mayor 5% Utilidades Netas del periodo anterior"), (0, "Menor al 5% Utilidades Netas del periodo anterior"))
INCUMPLIMIENTO = ((10, "SI"), (0, "NO"))
ACTIVIDAD = ((8, "SI"), (0, "NO"))
RECURRENTE = ((7, "Nueva Relacion"), (0, "Contrato Recurrente"))
TRANSVERSAL = ((5, "SI"), (0, "NO"))
INCIDENCIA = ((5, "ALTA INCIDENCIA"), (0, "POCA INCIDENCIA"))
MULTICONTRATO = ((5, "MAYOR A DOS"), (0, "DOS O MENOR"))
MARCO = ((5, "INFORMAL"), (0, "REGULADO"))


def get_resp(tupla, valor):
    for i in range(0, len(tupla)):
        if valor == tupla[i][0]:
            return tupla[i][1]


class Proveedor(models.Model):
    usuario                = models.ForeignKey(User, null=True, blank=True)
    codigo                 = models.CharField(max_length=15, verbose_name="Codigo del Proveedor")
    codigo_cliente         = models.CharField(max_length=15)
    nombre                 = models.CharField(max_length=125)
    actividad_economica    = models.CharField(max_length=125, verbose_name="Actividad Comercial", null=True)
    servicio               = models.CharField(max_length=125, verbose_name="Servicios Prestados")
    identificacion         = models.CharField(max_length=24, verbose_name="RUC/CEDULA")
    direccion              = models.TextField(max_length=600, null=True, blank=True)
    pago_anual             = models.FloatField(null=True, blank=True)
    forma_pago             = models.CharField(max_length=4, choices=FORMAS_PAGO)
    contacto               = models.CharField(max_length=120, null=True, blank=True)
    email                  = models.EmailField(max_length=120, null=True, blank=True)
    telefono               = models.CharField(max_length=60, null=True, blank=True)
    r_legal                = models.CharField(max_length=165, null=True, blank=True, verbose_name="Nombre del Representante Legal")
    buro                   = models.CharField(max_length=165, null=True, blank=True, verbose_name="calificacion de credito")
    cuenta_cordobas        = models.CharField(max_length=18, null=True, blank=True)
    beneficiario_cordobas  = models.CharField(max_length=160, null=True, blank=True)
    cuenta_dolares         = models.CharField(max_length=18, null=True, blank=True)
    beneficiario_dolares   = models.CharField(max_length=160, null=True, blank=True)
    relacionado            = models.BooleanField(default=False)
    contrato               = models.BooleanField(default=False)
    activo                 = models.BooleanField(default=True)

    temp_user              = models.CharField(max_length=125, null=True, blank=True)


    # Datos de la evaluacion anual

    importacia = models.PositiveIntegerField(null=True, choices=IMPORTANCIA, verbose_name="Importante para el funcionamiento estrategico del Banco y para atencion de clientes?")
    complejidad = models.PositiveIntegerField(null=True, choices=COMPLEJIDAD, verbose_name="Complejidad de la contratacion")
    reemplazo = models.PositiveIntegerField(null=True, choices=REEMPLAZO, verbose_name="Habilidad para reemplazar a la empresa por otra")
    credito = models.PositiveIntegerField(null=True, choices=CREDITO, verbose_name="Reputacion financiera y solvencia")
    anual = models.PositiveIntegerField(null=True, choices=ANUAL, verbose_name="Monto total anual pagado al proveedor")
    incumplimiento = models.PositiveIntegerField(null=True, choices=INCUMPLIMIENTO, verbose_name="La interrupcion del servicio genera incumplimiento regulatorio/legales al Banco")
    actividad = models.PositiveIntegerField(null=True, choices=ACTIVIDAD, verbose_name="Importancia de la actividad a ser contratada en relacion al giro principal de negocios de la institucion")
    recurrente = models.PositiveIntegerField(null=True, choices=RECURRENTE, verbose_name="Relacion del Proveedor de servicios con la institucion financiera")
    transversal = models.PositiveIntegerField(null=True, choices=TRANSVERSAL, verbose_name="Interrelacion de la operacion contratada con el resto de operacions de la institucion financiera")
    incidencia = models.PositiveIntegerField(null=True, choices=INCIDENCIA, verbose_name="Fallas del proveedor pone en riesgo las ganancias, solvencia, liquidez, capital, reputacion, fondeo o sistemas de control interno")
    multicontrato = models.PositiveIntegerField(null=True, choices=MULTICONTRATO, verbose_name="Existen mas de dos contratos vigentes con este mismo proveedor")
    marco = models.PositiveIntegerField(null=True, choices=MARCO, verbose_name="Marco regulatorio del proveedor")
    puntaje = models.PositiveIntegerField(null=True, default=0)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "proveedores"

    def evaluacion(self, campo):
        if campo:
            return int(campo)
        else:
            return 0

    def respuesta(self, campo):
        if campo:
            return campo
        else:
            return 0


    def calcular_puntaje(self):
	return self.evaluacion(self.importacia) \
      + self.evaluacion(self.complejidad) \
      + self.evaluacion(self.reemplazo) \
      + self.evaluacion(self.credito) \
      + self.evaluacion(self.anual) \
      + self.evaluacion(self.incumplimiento) \
      + self.evaluacion(self.actividad) \
      + self.evaluacion(self.recurrente) \
      + self.evaluacion(self.transversal) \
      + self.evaluacion(self.incidencia) \
      + self.evaluacion(self.multicontrato) \
      + self.evaluacion(self.marco)



    def get_user(self):
        nombre = self.temp_user.split(' ')[0]
        apellido = self.temp_user.split(' ')[1]
        usuario, created = User.objects.get_or_create(username=nombre[0].lower() + apellido.lower(), password="12345")
        return usuario



    def save(self, *args, **kwargs):
        self.puntaje = self.calcular_puntaje()
	super(Proveedor, self).save(*args, **kwargs)


class Expediente(models.Model):
    proveedor = models.ForeignKey(Proveedor)
    nombre = models.CharField(max_length=120)
    documento = models.FileField(upload_to="expedientes")
    fecha_vence = models.DateField()

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Expediente"







class nuevo(models.Model):
    cuenta = models.CharField(max_length=60, null=True)
    nombre = models.CharField(max_length=800, null=True)
    nivel = models.CharField(max_length=5, null=True)
    codigo_grupo = models.CharField(max_length=60, null=True)
    codigo_tipo_id_cdr = models.CharField(max_length=60, null=True)

    def relacionadas(self):
        return sectorizacion.objects.filter(nuevo=self)


class sectorizacion(models.Model):
    codigo_tipo_id = models.CharField(max_length=800, null=True)
    nombre_banca = models.CharField(max_length=800, null=True)
    nivel = models.CharField(max_length=5, null=True)
    codigo_grupo = models.CharField(max_length=60, null=True)
    descripcion_cliente = models.CharField(max_length=800, null=True)
    codigo_tipo_id_cdr = models.CharField(max_length=60, null=True)
    descripcion_cdr = models.CharField(max_length=800, null=True)

    nuevo = models.ForeignKey(nuevo, null=True)


    def sugeridos(self):
        resultados = []
        html = ""
        for palabra in self.nombre_banca.replace("(", "").replace(")", "").split(" "):
            if len(palabra) > 3:
                for a in nuevo.objects.filter(nombre__icontains=palabra).exclude(id__in=
                    sectorizacion.objects.filter(nuevo__isnull=False).values_list('nuevo', flat=True)):
                    if a not in resultados:
                        resultados.append(a)

        for n in resultados:
            html += "<p>"
            html += '<a class="sugerencia" data-sectorizacion="%s" data-nuevo="%s">%s - %s - %s</a>' % (self.id, n.id, n.id, n.cuenta, n.nombre)
        return html
    sugeridos.allow_tags = True


    def elegido(self):
        if self.nuevo:
            return self.nuevo.cuenta + " - " + self.nuevo.nombre
        else:
            return "Ninguno"




def datos_evaluacion(proveedores):
    data = []
    for p in proveedores:
        row = [p.codigo_cliente, p.nombre, p.actividad_economica, p.identificacion, p.direccion, p.contacto, p.telefono, p.pago_anual, p.buro, get_resp(IMPORTANCIA, p.importacia), p.importacia
              , get_resp(COMPLEJIDAD, p.complejidad), p.complejidad, get_resp(REEMPLAZO, p.reemplazo), p.reemplazo, get_resp(CREDITO, p.credito), p.credito
               , get_resp(ANUAL, p.anual), p.anual, get_resp(INCUMPLIMIENTO, p.incumplimiento), p.incumplimiento, get_resp(ACTIVIDAD, p.actividad), p.actividad
               , get_resp(RECURRENTE, p.recurrente), p.recurrente, get_resp(TRANSVERSAL, p.transversal), p.transversal, get_resp(INCIDENCIA, p.incidencia), p.incidencia
              , get_resp(MULTICONTRATO, p.multicontrato), p.multicontrato, get_resp(MARCO, p.marco), p.marco, p.puntaje
              ]
        data.append(row)
    return data

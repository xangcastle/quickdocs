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
CREDITO = ((10, "B, C, D y D o Ninguna"), (0, "Excelentes (A)"))
ANUAL = ((10, "Mayor 5% Utilidades Netas del periodo anterior"), (0, "Mayor 0% Utilidades Netas del periodo anterior"))
INCUMPLIMIENTO = ((10, "SI"), (0, "NO"))
ACTIVIDAD = ((8, "SI"), (0, "NO"))
RECURRENTE = ((7, "SI"), (0, "NO"))
TRANSVERSAL = ((5, "SI"), (0, "NO"))
INCIDENCIA = ((5, "ALTA INCIDENCIA"), (0, "POCA INCIDENCIA"))
MULTICONTRATO = ((5, "MAYOR A DOS"), (0, "DOS O MENOR"))
MARCO = ((5, "INFORMAL"), (0, "REGULADO"))


class Proveedor(models.Model):
    usuario                = models.ForeignKey(User, null=True, blank=True)
    codigo                 = models.CharField(max_length=15, verbose_name="Codigo del Proveedor")
    codigo_cliente         = models.CharField(max_length=15)
    nombre                 = models.CharField(max_length=125)
    actividad_economica    = models.CharField(max_length=125, verbose_name="Actividad Comercial", null=True)
    servicio               = models.CharField(max_length=125, verbose_name="Servicios Prestados")
    identificacion         = models.CharField(max_length=14, verbose_name="RUC/CEDULA")
    direccion              = models.TextField(max_length=600, null=True, blank=True)
    forma_pago             = models.CharField(max_length=4, choices=FORMAS_PAGO)
    contacto               = models.CharField(max_length=120, null=True, blank=True)
    email                  = models.EmailField(max_length=120, null=True, blank=True)
    telefono               = models.CharField(max_length=60, null=True, blank=True)
    r_legal                = models.CharField(max_length=165, null=True, blank=True, verbose_name="Nombre del Representante Legal")

    cuenta_cordobas        = models.CharField(max_length=18, null=True, blank=True)
    beneficiario_cordobas  = models.CharField(max_length=160, null=True, blank=True)
    cuenta_dolares         = models.CharField(max_length=18, null=True, blank=True)
    beneficiario_dolares   = models.CharField(max_length=160, null=True, blank=True)
    relacionado            = models.BooleanField(default=False)
    contrato               = models.BooleanField(default=False)
    activo                 = models.BooleanField(default=True)


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



class Expediente(models.Model):
    proveedor = models.ForeignKey(Proveedor)
    nombre = models.CharField(max_length=120)
    documento = models.FileField(upload_to="expedientes")
    fecha_vence = models.DateField()

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Expediente"

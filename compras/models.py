from django.db import models


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

class Proveedor(models.Model):

    codigo                 = models.CharField(max_length=15, verbose_name="Codigo del Proveedor")
    codigo_cliente         = models.CharField(max_length=15)
    nombre                 = models.CharField(max_length=125)
    actividad              = models.CharField(max_length=125, verbose_name="Actividad Comercial")
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

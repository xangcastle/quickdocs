from django.db import models


class Person(models.Model):
    MONEDAS = (
    ('CORDOBAS', 'CORDOBAS'),
    ('DOLARES', 'DOLARES'),
    )
    cedula = models.CharField(max_length=14)
    nombre = models.CharField(max_length=125, verbose_name="nombre completo")
    moneda = models.CharField(max_length=20, choices=MONEDAS, default="DOLARES")
    salario = models.FloatField(null=True)
    tc = models.FloatField(null=True, default=1.0)
    cuenta = models.CharField(max_length=25, null=True, verbose_name="cuenta a aplicar",
    help_text="cuenta banpro cordobas")
    fecha_ingreso = models.DateField(null=True, blank=True)
    deducciones = models.ManyToManyField('Deduccion', null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    def pago(self, dias):
        tarifa = round(self.salario / 30, 2)
        importe = round(tarifa * dias, 2)
        retension = round(importe * 0.1)
        return {
        'id': self.id,
        'cedula': self.cedula,
        'nombre': self.nombre,
        'salario': self.salario,
        'tarifa': tarifa,
        'importe': importe,
        'retension': retension,
        'deducciones': 0.0,
        'monto': round(importe - retension, 2)
        }

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Servicios Profesionales"


class Deduccion(models.Model):
    APLICABLES = (
    ("EMPLEADO", "EMPLEADO"),
    ("EMPLEADOR", "EMPLEADOR"),
    )
    nombre = models.CharField(max_length=65)
    porcent = models.FloatField(verbose_name="porcentaje a aplicar %")
    auxiliar = models.CharField(max_length=4, null=True)
    cuenta = models.CharField(max_length=25, null=True,
    verbose_name="cuenta contable")
    aplica = models.CharField(max_length=15, choices=APLICABLES,
    default="EMPLEADO")

    class Meta:
        verbose_name_plural = "deducciones"

    def __unicode__(self):
        return ("%s %s" % (self.nombre, str(round(self.porcent, 2)))) + "%"

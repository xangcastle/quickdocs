from django.db import models


class Person(models.Model):
    cedula = models.CharField(max_length=14)
    nombre = models.CharField(max_length=125, verbose_name="nombre completo")
    salario = models.FloatField(null=True)
    fecha_ingreso = models.DateField(null=True, blank=True)

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
        verbose_name_plural = "Servicios Profecionales"

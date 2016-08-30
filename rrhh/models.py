from django.db import models


class Person(models.Model):
    cedula = models.CharField(max_length=14)
    nombre = models.CharField(max_length=125, verbose_name="nombre completo")
    salario = models.FloatField(null=True)
    fecha_ingreso = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Servicios Profecionales"

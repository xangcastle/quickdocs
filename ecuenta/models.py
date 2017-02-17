from django.db import models


class Paquete(models.Model):
    consecutivo = models.PositiveIntegerField(null=True)
    num_paquete = models.PositiveIntegerField(null=True)
    direccion = models.CharField(max_length=400, null=True)
    linea = models.PositiveIntegerField(null=True)
    cuenta = models.CharField(max_length=20)
    emision = models.CharField(max_length=65, null=True)
    tipo_origen = models.CharField(max_length=2, null=True)
    reenvio = models.CharField(max_length=2, null=True)
    anexado = models.CharField(max_length=2, null=True)
    cf_cliente = models.CharField(max_length=165, null=True, verbose_name="Nombre del Cliente")
    cf_direccion = models.CharField(max_length=400, null=True)
    cf_origen = models.CharField(max_length=25, null=True)


    # campos para control de entregas

    entregado = models.BooleanField(default=False)
    fecha_entrega = models.DateTimeField(null=True)
    recibe = models.CharField(max_length=165, null=True)
    entrega = models.CharField(max_length=165, null=True)


    def __unicode__(self):
        return "Paquete No " + str(self.num_paquete)

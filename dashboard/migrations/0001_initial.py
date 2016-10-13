# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emboso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NUM_TARJETA', models.CharField(max_length=20)),
                ('FECHA_EMBOZO', models.DateField()),
                ('ESTADO_CTA', models.CharField(max_length=12)),
                ('ESTADO_TJT', models.CharField(max_length=12)),
                ('ESTADO_BODEGA', models.CharField(max_length=12)),
                ('ESTADO_PAQ', models.CharField(max_length=12)),
                ('ESTADO_MON', models.CharField(max_length=12)),
                ('FECHA_SALIDA', models.DateField()),
                ('FECHA_RETORNO', models.DateField()),
                ('TIPO_ENTRADA', models.CharField(max_length=12)),
                ('UBICA_RETORNO', models.CharField(max_length=50)),
                ('ORIGEN', models.CharField(max_length=50)),
                ('ZONA', models.CharField(max_length=50)),
                ('TIPO_TARJETA', models.CharField(max_length=50)),
                ('REG_FISICO', models.DateField()),
                ('COD_REVISION', models.CharField(max_length=12)),
                ('OBS_REVISION', models.CharField(max_length=200)),
                ('POSICION', models.IntegerField()),
                ('UBICACION', models.CharField(max_length=50)),
                ('NUM_SOLIC', models.IntegerField()),
                ('NUM_CUENTA', models.CharField(max_length=20)),
                ('COD_CLIENTE', models.IntegerField()),
                ('NOM_CLIENTE', models.CharField(max_length=200)),
                ('CANTIDAD_SALIDA', models.IntegerField()),
                ('PRODUCTO', models.IntegerField()),
                ('DES_PRODUCTO', models.CharField(max_length=90)),
                ('IND_INVENTARIO', models.CharField(max_length=1)),
                ('IND_BODEGA', models.CharField(max_length=1)),
                ('AGENCIA_CUSTODIO', models.IntegerField()),
                ('USUARIO_PAQUETE', models.CharField(max_length=60)),
                ('NUM_PAQUETE', models.IntegerField()),
                ('FEC_ASIGNA_PAQ', models.DateField()),
                ('FEC_DESCARGA_PAQ', models.DateField()),
                ('COD_CONTRATO', models.IntegerField()),
                ('DESCONTRATO', models.CharField(max_length=200)),
                ('CODCTACTO', models.IntegerField()),
                ('NOMCTACTO', models.CharField(max_length=60)),
                ('SUCURSAL', models.CharField(max_length=60)),
                ('BANDEJA', models.CharField(max_length=60)),
                ('USR_TM', models.CharField(max_length=60)),
                ('INDFUENTE', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

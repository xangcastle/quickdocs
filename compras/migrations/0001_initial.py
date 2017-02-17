# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=15)),
                ('codigo_cliente', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=125)),
                ('actividad', models.CharField(max_length=125, verbose_name=b'Actividad Comercial')),
                ('servicio', models.CharField(max_length=125, verbose_name=b'Servicios Prestados')),
                ('identificacion', models.CharField(max_length=14, verbose_name=b'RUC/CEDULA')),
                ('direccion', models.TextField(max_length=600, null=True, blank=True)),
                ('forma_pago', models.CharField(max_length=4, choices=[(b'NC', b'NOTA DE CREDITO'), (b'CK', b'CHEQUE'), (b'TFI', b'TRANSFERENCIA INTERNACIONAL'), (b'TFCI', b'TRANSFERENCIA CUENTA INTEGRA')])),
                ('contacto', models.CharField(max_length=120, null=True, blank=True)),
                ('email', models.EmailField(max_length=120, null=True, blank=True)),
                ('telefono', models.CharField(max_length=60, null=True, blank=True)),
                ('r_legal', models.CharField(max_length=165, null=True, verbose_name=b'Nombre del Representante Legal', blank=True)),
                ('cuenta_cordobas', models.CharField(max_length=18, null=True, blank=True)),
                ('beneficiario_cordobas', models.CharField(max_length=160, null=True, blank=True)),
                ('cuenta_dolares', models.CharField(max_length=18, null=True, blank=True)),
                ('beneficiario_dolares', models.CharField(max_length=160, null=True, blank=True)),
                ('relacionado', models.BooleanField(default=False)),
                ('contrato', models.BooleanField(default=False)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'proveedores',
            },
            bases=(models.Model,),
        ),
    ]

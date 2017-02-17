# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
                ('documento', models.FileField(upload_to=b'expedientes')),
                ('fecha_vence', models.DateField()),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Expediente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=15, verbose_name=b'Codigo del Proveedor')),
                ('codigo_cliente', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=125)),
                ('actividad_economica', models.CharField(max_length=125, null=True, verbose_name=b'Actividad Comercial')),
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
                ('importacia', models.PositiveIntegerField(null=True, verbose_name=b'Importante para el funcionamiento estrategico del Banco y para atencion de clientes?', choices=[(15, b'SI'), (0, b'NO')])),
                ('complejidad', models.PositiveIntegerField(null=True, verbose_name=b'Complejidad de la contratacion', choices=[(10, b'ALTA'), (0, b'BAJA')])),
                ('reemplazo', models.PositiveIntegerField(null=True, verbose_name=b'Habilidad para reemplazar a la empresa por otra', choices=[(10, b'ALTA COMPLEJIDAD'), (0, b'COMPLEJIDAD ACEPTABLE')])),
                ('credito', models.PositiveIntegerField(null=True, verbose_name=b'Reputacion financiera y solvencia', choices=[(10, b'B, C, D y D o Ninguna'), (0, b'Excelentes (A)')])),
                ('anual', models.PositiveIntegerField(null=True, verbose_name=b'Monto total anual pagado al proveedor', choices=[(10, b'Mayor 5% Utilidades Netas del periodo anterior'), (0, b'Mayor 0% Utilidades Netas del periodo anterior')])),
                ('incumplimiento', models.PositiveIntegerField(null=True, verbose_name=b'La interrupcion del servicio genera incumplimiento regulatorio/legales al Banco', choices=[(10, b'SI'), (0, b'NO')])),
                ('actividad', models.PositiveIntegerField(null=True, verbose_name=b'Importancia de la actividad a ser contratada en relacion al giro principal de negocios de la institucion', choices=[(8, b'SI'), (0, b'NO')])),
                ('recurrente', models.PositiveIntegerField(null=True, verbose_name=b'Relacion del Proveedor de servicios con la institucion financiera', choices=[(7, b'SI'), (0, b'NO')])),
                ('transversal', models.PositiveIntegerField(null=True, verbose_name=b'Interrelacion de la operacion contratada con el resto de operacions de la institucion financiera', choices=[(5, b'SI'), (0, b'NO')])),
                ('incidencia', models.PositiveIntegerField(null=True, verbose_name=b'Fallas del proveedor pone en riesgo las ganancias, solvencia, liquidez, capital, reputacion, fondeo o sistemas de control interno', choices=[(5, b'ALTA INCIDENCIA'), (0, b'POCA INCIDENCIA')])),
                ('multicontrato', models.PositiveIntegerField(null=True, verbose_name=b'Existen mas de dos contratos vigentes con este mismo proveedor', choices=[(5, b'MAYOR A DOS'), (0, b'DOS O MENOR')])),
                ('marco', models.PositiveIntegerField(null=True, verbose_name=b'Marco regulatorio del proveedor', choices=[(5, b'INFORMAL'), (0, b'REGULADO')])),
                ('puntaje', models.PositiveIntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name_plural': 'proveedores',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='expediente',
            name='proveedor',
            field=models.ForeignKey(to='compras.Proveedor'),
            preserve_default=True,
        ),
    ]

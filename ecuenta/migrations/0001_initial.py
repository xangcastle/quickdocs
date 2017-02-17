# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consecutivo', models.PositiveIntegerField(null=True)),
                ('num_paquete', models.PositiveIntegerField(null=True)),
                ('direccion', models.CharField(max_length=400, null=True)),
                ('linea', models.PositiveIntegerField(null=True)),
                ('cuenta', models.CharField(max_length=20)),
                ('emision', models.CharField(max_length=65, null=True)),
                ('tipo_origen', models.CharField(max_length=2, null=True)),
                ('reenvio', models.CharField(max_length=2, null=True)),
                ('anexado', models.CharField(max_length=2, null=True)),
                ('cf_cliente', models.CharField(max_length=2, null=True)),
                ('cf_direccion', models.CharField(max_length=400, null=True)),
                ('cf_origen', models.CharField(max_length=25, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

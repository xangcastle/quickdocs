# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_proveedor_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='nuevo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cuenta', models.CharField(max_length=60, null=True)),
                ('nombre', models.CharField(max_length=800, null=True)),
                ('nivel', models.CharField(max_length=5, null=True)),
                ('codigo_grupo', models.CharField(max_length=60, null=True)),
                ('codigo_tipo_id_cdr', models.CharField(max_length=60, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sectorizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_tipo_id', models.CharField(max_length=800, null=True)),
                ('nombre_banca', models.CharField(max_length=800, null=True)),
                ('nivel', models.CharField(max_length=5, null=True)),
                ('codigo_grupo', models.CharField(max_length=60, null=True)),
                ('descripcion_cliente', models.CharField(max_length=800, null=True)),
                ('codigo_tipo_id_cdr', models.CharField(max_length=60, null=True)),
                ('descripcion_cdr', models.CharField(max_length=800, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

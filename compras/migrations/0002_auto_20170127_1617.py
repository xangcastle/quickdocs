# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
                ('documento', models.FileField(upload_to=b'expedientes')),
                ('fecha_vence', models.DateField()),
                ('proveedor', models.ForeignKey(to='compras.Proveedor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='codigo',
            field=models.CharField(max_length=15, verbose_name=b'Codigo del Proveedor'),
        ),
    ]

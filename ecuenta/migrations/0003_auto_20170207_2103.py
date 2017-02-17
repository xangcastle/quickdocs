# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecuenta', '0002_auto_20170207_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='entregado',
            field=models.CharField(max_length=165, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='paquete',
            name='fecha_entrega',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='paquete',
            name='recibido',
            field=models.CharField(max_length=165, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='paquete',
            name='cf_cliente',
            field=models.CharField(max_length=165, null=True, verbose_name=b'Nombre del Cliente'),
        ),
    ]

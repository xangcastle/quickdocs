# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0007_auto_20170221_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='anual',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Monto total anual pagado al proveedor', choices=[(10, b'Mayor 5% Utilidades Netas del periodo anterior'), (0, b'Menor al 5% Utilidades Netas del periodo anterior')]),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='credito',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Reputacion financiera y solvencia', choices=[(10, b'B, C, D y D o Ninguna'), (0, b'Excelentes (A)'), (0, b'No encontrado'), (0, b'Ninguna')]),
        ),
    ]

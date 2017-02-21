# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_auto_20170221_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='pago_anual',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

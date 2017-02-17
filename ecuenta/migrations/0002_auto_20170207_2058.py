# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecuenta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='cf_cliente',
            field=models.CharField(max_length=165, null=True),
        ),
    ]

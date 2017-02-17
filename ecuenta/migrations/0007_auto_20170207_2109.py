# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecuenta', '0006_auto_20170207_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paquete',
            old_name='entregado_temp',
            new_name='entregado',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecuenta', '0005_paquete_entregado_temp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paquete',
            old_name='entregado',
            new_name='entrega',
        ),
    ]

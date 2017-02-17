# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecuenta', '0003_auto_20170207_2103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paquete',
            old_name='recibido',
            new_name='recibe',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_emboso_usr_tm'),
    ]

    operations = [
        migrations.AddField(
            model_name='emboso',
            name='USR_TM',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
    ]

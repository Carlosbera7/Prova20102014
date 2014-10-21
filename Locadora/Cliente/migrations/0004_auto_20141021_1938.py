# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0003_auto_20141021_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='Celular',
            field=models.IntegerField(null=True, verbose_name=b'Celular'),
        ),
    ]

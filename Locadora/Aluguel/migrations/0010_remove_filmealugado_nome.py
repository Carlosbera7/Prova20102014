# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aluguel', '0009_auto_20141021_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filmealugado',
            name='Nome',
        ),
    ]

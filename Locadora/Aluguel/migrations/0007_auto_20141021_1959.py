# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aluguel', '0006_auto_20141021_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluguel',
            options={'verbose_name': 'Aluguel', 'verbose_name_plural': 'Aluguel de Filme'},
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aluguel', '0004_filmealugado'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='DataLocacao',
            field=models.DateField(null=True, verbose_name=b'Data Devolucao'),
            preserve_default=True,
        ),
    ]

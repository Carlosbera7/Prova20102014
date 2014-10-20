# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0002_auto_20141020_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='Genero',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Genero do Filme', choices=[(b'R', b'ROMANCE'), (b'C', b'COMEDIA'), (b'A', b'ACAO'), (b'D', b'DRAMA'), (b'G', b'GUERRA'), (b'T', b'TERROR')]),
        ),
    ]

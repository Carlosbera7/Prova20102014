# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0003_auto_20141020_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='Categoria',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Categoria do Filme', choices=[(b'P', b'PROMOCAO'), (b'C', b'CATALOGO'), (b'L', b'LANCAMENTO')]),
        ),
    ]

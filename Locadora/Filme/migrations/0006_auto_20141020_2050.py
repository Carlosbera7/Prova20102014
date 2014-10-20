# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0005_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='valor',
            name='Categoria',
            field=models.ForeignKey(verbose_name=b'Categoia', to='Filme.filme', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='valor',
            name='Preco',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Preco'),
        ),
    ]

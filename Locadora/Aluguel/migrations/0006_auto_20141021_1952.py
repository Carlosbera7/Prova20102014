# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0007_auto_20141021_1921'),
        ('Aluguel', '0005_aluguel_datalocacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluguel',
            name='TituloFilme',
        ),
        migrations.RemoveField(
            model_name='filmealugado',
            name='NomeFilme',
        ),
        migrations.AddField(
            model_name='filmealugado',
            name='NomeAluguel',
            field=models.ForeignKey(verbose_name=b'Filme', to='Aluguel.aluguel', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='filmealugado',
            name='TituloFilme',
            field=models.ForeignKey(verbose_name=b'Filme', to='Filme.filme', null=True),
            preserve_default=True,
        ),
    ]

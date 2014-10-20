# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aluguel', '0002_auto_20141020_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguel',
            name='Nome',
            field=models.ForeignKey(verbose_name=b'Cliente', to='Cliente.Pessoa', null=True),
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='TituloFilme',
            field=models.ForeignKey(verbose_name=b'Filme', to='Filme.filme', null=True),
        ),
    ]

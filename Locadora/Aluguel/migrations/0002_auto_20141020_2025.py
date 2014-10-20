# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0001_initial'),
        ('Filme', '0004_auto_20141020_2025'),
        ('Aluguel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='Nome',
            field=models.ForeignKey(default=1, verbose_name=b'Cliente', to='Cliente.Pessoa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluguel',
            name='TituloFilme',
            field=models.ForeignKey(default=2, verbose_name=b'Filme', to='Filme.filme'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0004_auto_20141021_1938'),
        ('Aluguel', '0007_auto_20141021_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmealugado',
            name='Nome',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='Cliente.Pessoa', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='filmealugado',
            name='NomeAluguel',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='Aluguel.aluguel', null=True),
        ),
    ]

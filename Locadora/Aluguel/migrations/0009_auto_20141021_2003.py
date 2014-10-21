# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aluguel', '0008_auto_20141021_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmealugado',
            name='NomeAluguel',
            field=models.ForeignKey(verbose_name=b'Aluguel', to='Aluguel.aluguel', null=True),
        ),
    ]

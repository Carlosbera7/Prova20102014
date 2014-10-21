# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aluguel', '0003_auto_20141020_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmeAlugado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NomeFilme', models.ForeignKey(verbose_name=b'Cliente', to='Aluguel.aluguel', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

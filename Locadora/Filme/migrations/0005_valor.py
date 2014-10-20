# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0004_auto_20141020_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Preco', models.ForeignKey(verbose_name=b'Preco', to='Filme.filme')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

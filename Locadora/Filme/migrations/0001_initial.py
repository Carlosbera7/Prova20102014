# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TituloFilme', models.CharField(max_length=100, null=True, verbose_name=b'Titulo do Filme')),
                ('Genero', models.CharField(max_length=100, null=True, verbose_name=b'Genero do Filme')),
                ('Categoria', models.CharField(max_length=100, null=True, verbose_name=b'Categoria do Filme')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

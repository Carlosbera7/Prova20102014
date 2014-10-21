# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0006_auto_20141020_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NomeCategoria', models.CharField(max_length=100, null=True, verbose_name=b'Nome Categoria')),
                ('ValorCategoria', models.CharField(max_length=10, null=True, verbose_name=b'Valor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='valor',
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Valor',
        ),
        migrations.AlterField(
            model_name='filme',
            name='Categoria',
            field=models.ForeignKey(verbose_name=b'Categoria', to='Filme.Categoria', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0002_remove_pessoa_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='CPF',
            field=models.IntegerField(null=True, verbose_name=b'CPF'),
        ),
    ]

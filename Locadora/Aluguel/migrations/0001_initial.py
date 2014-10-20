# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aluguel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DataDevolucao', models.DateField(null=True, verbose_name=b'Data Devolucao')),
                ('Pagamento', models.CharField(max_length=1, null=True, verbose_name=b'Pagamento', choices=[(b'V', b'PAGO'), (b'P', b'A PAGAR')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

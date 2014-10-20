#coding:utf-8
from django.db import models

PAGAMENTO_OPCOES = [

	('V','PAGO'),
	('P','A PAGAR')
	
]

class aluguel (models.Model):
	Nome = models.ForeignKey("Cliente.Pessoa",verbose_name="Cliente",null=True)
	TituloFilme = models.ForeignKey("Filme.filme",verbose_name="Filme",null=True)
	DataDevolucao = models.DateField('Data Devolucao',null=True)
	Pagamento = models.CharField('Pagamento',max_length=1,choices=PAGAMENTO_OPCOES,null=True)




# Create your models here.

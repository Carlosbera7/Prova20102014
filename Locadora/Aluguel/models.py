#coding:utf-8
from django.db import models

PAGAMENTO_OPCOES = [

	('V','PAGO'),
	('P','A PAGAR')
	
]

class aluguel (models.Model):
	Nome = models.ForeignKey("Cliente.Pessoa",verbose_name="Cliente",null=True)
	#TituloFilme = models.ForeignKey("Filme.filme",verbose_name="Filme",null=True)
	DataLocacao = models.DateField('Data Devolucao',null=True)
	DataDevolucao = models.DateField('Data Devolucao',null=True)
	Pagamento = models.CharField('Pagamento',max_length=1,choices=PAGAMENTO_OPCOES,null=True)
		
	class Meta:
		verbose_name = "Aluguel"
		verbose_name_plural = "Aluguel de Filme"
	
	
	#def  __unicode__(self):
		#return self.DataDevolucao
	
class FilmeAlugado (models.Model):
	TituloFilme = models.ForeignKey("Filme.filme",verbose_name="Filme",null=True)
	NomeAluguel = models.ForeignKey(aluguel,verbose_name="Aluguel",null=True)
	#Nome = models.ForeignKey("Cliente.Pessoa",verbose_name="Pessoa",null=True)
	
	
	#def  __unicode__(self):
		#return self.TituloFilme




# Create your models here.

#coding:utf-8
from django.db import models

# Create your models here.
GENERO_OPCOES = [

	('R','ROMANCE'),
	('C','COMEDIA'),
	('A','ACAO'),
	('D','DRAMA'),
	('G','GUERRA'),
	('T','TERROR')
]



class Categoria(models.Model):
	NomeCategoria = models.CharField('Nome Categoria',max_length=100,null=True)
	ValorCategoria = models.CharField('Valor',max_length=10,null=True)
	
	
	def __unicode__(self):
		return self.NomeCategoria
	
	


class filme(models.Model):
	TituloFilme = models.CharField('Titulo do Filme',max_length=100,null=True)
	Genero = models.CharField('Genero do Filme',max_length=1,choices=GENERO_OPCOES,null=True)
	Categoria = models.ForeignKey(Categoria,verbose_name="Categoria",null=True)
	

	def __unicode__(self):
		return self.TituloFilme
		
	
		
	


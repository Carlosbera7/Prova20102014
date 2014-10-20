#coding:utf-8
from django.db import models

# Create your models here.
GENERO_OPCOES = [

	('R','ROMANCE'),
	('C','COMEDIA'),
	('A','ACAO'),
	('D','DRAMA'),
	('G','GUERRA'),
	('T','TERROR'),
]

CATEGORIA_OPCOES = [

	('P','PROMOCAO'),
	('C','CATALOGO'),
	('L','LANCAMENTO'),
	
]

class filme(models.Model):
	TituloFilme = models.CharField('Titulo do Filme',max_length=100,null=True)
	Genero = models.CharField('Genero do Filme',max_length=1,choices=GENERO_OPCOES,null=True)
	Categoria = models.CharField('Categoria do Filme',max_length=1,choices=CATEGORIA_OPCOES,null=True)
	
class Valor(models.Model):
	#TituloFilme = models.ForeignKey(filme,verbose_name="Titulo Filme",null=True)
	#Genero = models.ForeignKey(filme,verbose_name="Genero",null=True)
	Categoria = models.ForeignKey(filme,verbose_name="Categoia",null=True)	
	Preco = models.CharField('Preco',max_length=10,null=True)

   
	def __unicode__(self):
		return self.TituloFilme


#coding:utf-8
from django.db import models

# Create your models here.
SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino')
]

class Pessoa (models.Model):
	Nome = models.CharField('Nome',max_length=100,null=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	CPF = models.CharField('CPF',max_length=15,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	
	
	def __unicode__(self):
		return self.Nome


#coding:utf-8
from django.contrib import admin
from models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
	list_display = ['Nome','Sexo','DataNascimento']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True
	
admin.site.register(Pessoa,PessoaAdmin)

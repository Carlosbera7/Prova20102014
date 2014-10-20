#coding:utf-8
from django.contrib import admin
from models import filme
from models import Valor

class FilmesAdmin(admin.ModelAdmin):
	list_display = ['TituloFilme','Genero','Categoria']
	list_filter = ['TituloFilme']
	search_fields = ['TituloFilme']
	save_as = True
	
class ValorAdmin(admin.ModelAdmin):
	list_display = ['Categoria','Preco']
	list_filter = ['Categoria','Preco']
	search_fields = ['Categoria','Preco']
	save_as = True
		
admin.site.register(filme,FilmesAdmin)
admin.site.register(Valor,ValorAdmin)

# Register your models here.

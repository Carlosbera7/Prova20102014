#coding:utf-8
from django.contrib import admin
from models import filme
from models import Categoria

class FilmesAdmin(admin.ModelAdmin):
	list_display = ['TituloFilme','Genero']
	list_filter = ['TituloFilme']
	search_fields = ['TituloFilme']
	save_as = True
	
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ['NomeCategoria','ValorCategoria']
	list_filter = ['NomeCategoria','ValorCategoria']
	search_fields = ['NomeCategoria','ValorCategoria']
	save_as = True
		
admin.site.register(filme,FilmesAdmin)
admin.site.register(Categoria,CategoriaAdmin)

# Register your models here.

#coding:utf-8
from django.contrib import admin
from models import aluguel
from models import FilmeAlugado

class FilmesInline(admin.TabularInline):
	model = FilmeAlugado

class AluguelAdmin(admin.ModelAdmin):
	list_display = ['Nome','DataDevolucao','Pagamento']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True
	
	inlines = [FilmesInline]

class FilmeAlugadoAdmin(admin.ModelAdmin):
	list_display = ['TituloFilme']
	list_filter = ['TituloFilme']
	search_fields = ['TituloFilme']
	save_as = True	
	
	
admin.site.register(aluguel,AluguelAdmin)
admin.site.register(FilmeAlugado,FilmeAlugadoAdmin)

#coding:utf-8
from django.contrib import admin
from models import aluguel

#class FilmesInline(admin.TabularInline):
#	model = aluguel

class AluguelAdmin(admin.ModelAdmin):
	list_display = ['Nome','TituloFilme','DataDevolucao','Pagamento']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True
	
	#inlines = [FilmesInline]
	
admin.site.register(aluguel,AluguelAdmin)

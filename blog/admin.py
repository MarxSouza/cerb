from django.contrib import admin
from . import models
		
class CategoriaAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}

class NoticiaAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}
	exclude = ['autor', 'visualizacoes']
	list_display = ['titulo', 'categoria', 'data_de_publicacao', 'autor']
	list_filter = ['data_de_publicacao']
	search_fields = ["titulo", "texto"]

	def save_model(self, request, obj, form, change):
		obj.autor = request.user
		obj.save()
	
admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Noticia, NoticiaAdmin)
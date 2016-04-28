from django.contrib import admin
from django.utils import timezone
from . import models
		
class CategoriaAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}

class NoticiaAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}
	exclude = ['autor', 'views', 'data_de_publicacao']
	list_display = ['titulo', 'categoria', 'data_de_publicacao', 'autor']
	list_filter = ['data_de_publicacao']
	search_fields = ["titulo", "texto"]

	def save_model(self, request, obj, form, change):
		obj.autor = request.user.get_full_name()
		obj.data_de_publicacao = timezone.now()
		obj.save()
	
admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Noticia, NoticiaAdmin)
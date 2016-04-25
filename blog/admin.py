from django.contrib import admin
from . import models

class ColunistaAdmin(admin.ModelAdmin):
	pass

class CategoriaAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}

class NoticiaAdmin(admin.ModelAdmin):
	exclude = ['autor']
	prepopulated_fields = {'slug': ('titulo',)}
	list_display = ['titulo', 'categoria', 'data_de_publicacao']
	list_filter = ['data_de_publicacao']
	search_fields = ["titulo", "texto"]

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()	


admin.site.register(models.Colunista, ColunistaAdmin)
admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Noticia, NoticiaAdmin)
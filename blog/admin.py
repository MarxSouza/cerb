from django.contrib import admin
from django.utils import timezone
from django import forms
from blog.models import Categoria, Noticia
		
class CategoriaAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}

class NoticiaAdmin(admin.ModelAdmin):
    exclude = ['autor', 'views', 'data_de_publicacao']
    prepopulated_fields = {'slug': ('titulo',)}
    list_display = ['titulo', 'categoria', 'data_de_publicacao', 'autor']
    list_filter = ['data_de_publicacao']
    search_fields = ["titulo", "texto"]

    def save_model(self, request, obj, form, change):
    	categorias = Categoria.objects.filter(colunista=request.user).order_by('titulo').all()
    	obj.autor = request.user.get_full_name()
    	obj.data_de_publicacao = timezone.now()
    	for x in categorias:
    		if obj.categoria == x:
    			obj.save()

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
from django.contrib import admin
from . import models

class ProjetoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'titulo':('slug',)}
admin.site.register(models.Projeto, ProjetoAdmin)    

admin.site.register(models.Informacao)
admin.site.register(models.Funcionario)

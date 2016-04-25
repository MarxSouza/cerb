from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Noticia(models.Model): 
	autor = models.ForeignKey('blog.Colunista', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=100, verbose_name="Título")
	categoria = models.ForeignKey('blog.Categoria')
	imagem = models.ImageField(upload_to='noticias')
	texto = models.TextField()
	slug = models.SlugField()
	data_de_publicacao = models.DateTimeField(verbose_name="Data de Publicação", default=timezone.now())
	
	def __str__(self):
		return "%s - %s" % (self.titulo, self.categoria)

class Categoria(models.Model): 
	titulo = models.CharField(max_length=100, verbose_name="Título")
	slug = models.SlugField()

	def __str__(self):
		return self.titulo

class Colunista(models.Model):
	usuario = models.OneToOneField(User, verbose_name="Usuário")
	categoria = models.ForeignKey(Categoria, default=1)
	bio = models.TextField(help_text="Biografia do Autor")

	def __str__(self):
		return self.usuario.get_full_name()

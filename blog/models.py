from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

categorias = (
	('Automobilismo','Automobilismo'),
	('Educação','Educação'),
	('Esporte','Esporte'),
	('Moda','Moda'),
	('Política','Política'),
)

class Noticia(models.Model): 
	autor = models.OneToOneField(User, null=True)
	titulo = models.CharField(max_length=100, verbose_name="Título")
	categoria = models.ForeignKey('blog.Categoria', default=1)
	imagem = models.ImageField(upload_to='noticias', blank=True)
	texto = models.TextField()
	visualizacoes = models.PositiveIntegerField(default=0)
	data_de_publicacao = models.DateTimeField(verbose_name="Data de Publicação", default=timezone.now())
	slug = models.SlugField()
	
	def __str__(self):
		return "%s - %s" % (self.titulo, self.categoria)

class Categoria(models.Model): 
	titulo = models.CharField(max_length=100, verbose_name="Título", choices=categorias)
	slug = models.SlugField()

	def __str__(self):
		return self.titulo
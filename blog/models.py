from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

categorias = (
	('Educação','Educação'),
	('Esporte','Esporte'),
	('Moda','Moda'),
	('Política','Política'),
	('Tecnologia','Tecnologia'),
	('Saúde','Saúde'),
	('Fatos Corriqueiros','Fatos Corriqueiros'),
	('Música', 'Música'),
)

class Categoria(models.Model): 
	titulo = models.CharField(max_length=100, verbose_name="Título", choices=categorias)
	colunista = models.ForeignKey(User)
	slug = models.SlugField()

	def __str__(self):
		return self.titulo

class Noticia(models.Model): 
	imagem = models.ImageField(upload_to='noticias', blank=True)
	autor = models.CharField(max_length=200)
	titulo = models.CharField(max_length=100, verbose_name="Título")
	categoria = models.ForeignKey(Categoria, default=1)
	texto = RichTextField()
	views = models.PositiveIntegerField(default=0)
	data_de_publicacao = models.DateTimeField(verbose_name="Data de Publicação")
	slug = models.SlugField()
	
	def __str__(self):
		return "%s - %s:%s" % (self.titulo, self.autor, self.categoria)


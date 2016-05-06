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
	('Culinária','Culinária'),
	('Fatos Corriqueiros','Fatos Corriqueiros'),
	('Música', 'Música'),
	('Religião','Religião'),
	('Cultura','Cultura'),
)

class Categoria(models.Model): 
	titulo = models.CharField(max_length=100, verbose_name="Título", choices=categorias)
	colunista = models.ForeignKey(User)
	slug = models.SlugField()

	def __str__(self):
		return self.titulo

class Noticia(models.Model): 
	imagem = models.ImageField(upload_to='noticias', blank=True)
	titulo = models.CharField(max_length=100, verbose_name="Título")
	autor = models.CharField(max_length=200)
	categoria = models.ForeignKey(Categoria, default=1)
	texto = RichTextField()
	views = models.PositiveIntegerField(default=0)
	slug = models.SlugField()
	data_de_publicacao = models.DateTimeField(verbose_name="Data de Publicação")
	
	def __str__(self):
		return "%s / %s" % (self.titulo, self.categoria)
	
class Comentario(models.Model):
	noticias = models.ForeignKey('blog.Noticia', related_name='comentarios')
	autor = models.CharField(max_length=200)
	texto = models.TextField()
	data = models.DateTimeField(default=timezone.now)
	verificacao = models.BooleanField(default=False)

	def verificar(self):
		self.aprovacao = True
		self.save()

	def __str__(self):
		return self.texto
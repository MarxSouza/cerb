from django.db import models

class Projeto(models.Model):
	titulo = models.CharField(max_length=100)
	tema = models.CharField(max_length=100)
	imagem = models.ImageField(upload_to='projetos')
	descricao = models.TextField(verbose_name='Descrição')
	data_de_realizacao = models.DateTimeField(verbose_name='Data de realização')
	local_de_realizacao = models.CharField(max_length=300, verbose_name='Local de realização')
	slug = models.SlugField(default='')
	
	def __str__(self):
		return "%s - %s" % (self.titulo, self.data_de_realizacao)

class Informacao(models.Model):
	titulo = models.CharField(max_length=100)
	descricao = models.TextField(verbose_name='Descrição')

	def __str__(self):
		return self.titulo

class Funcionario(models.Model):
	nome = models.CharField(max_length=100)
	foto = models.ImageField(upload_to='funcionarios')
	profissao = models.CharField(max_length=100)
	email = models.EmailField()
	bio = models.TextField(verbose_name='Biografia', help_text='Biografia do Funcionário')
	facebook = models.URLField(help_text='Link para perfil')
	twitter = models.URLField(help_text='Link para perfil')
	linkedin = models.URLField(help_text='Link para perfil')
	
	def __str__(self):
		return "%s - %s - %s" % (self.nome, self.email, self.profissao)

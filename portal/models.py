from django.db import models

class Informacao(models.Model):
	titulo = models.CharField(max_length=100)
	descricao = models.TextField(verbose_name='Descrição')

	def __str__(self):
		return self.titulo

class Funcionario(models.Model):
	nome = models.CharField(max_length=100)
	foto = models.ImageField(upload_to='funcionarios', blank=True)
	profissao = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	bio = models.TextField(verbose_name='Biografia', help_text='Biografia do Funcionário')
	facebook = models.URLField(help_text='Link para perfil', blank=True)
	twitter = models.URLField(help_text='Link para perfil', blank=True)
	linkedin = models.URLField(help_text='Link para perfil', blank=True)
	
	def __str__(self):
		return "%s - %s - %s" % (self.nome, self.email, self.profissao)

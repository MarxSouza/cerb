from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .models import Projeto, Informacao, Funcionario
from blog.models import Noticia
from .forms import ContatoForm
from cerb import settings

def index(request):
	noticias = Noticia.objects.all().order_by('-data_de_publicacao')
	if not noticias:
		messages.info(request, 'Não foi possivel carregar as noticias')
	projetos = Projeto.objects.all().order_by('-data_de_realizacao')
	if not projetos:
		messages.error(request, 'Não foi possivel carregar os projetos')
	return render(request, 'portal/index.html', {'noticias':noticias, 'projetos':projetos})

def projetos(request):
	projetos = Projeto.objects.all().order_by('-data_de_realizacao')
	return render(request, 'portal/projetos.html', {'projetos':projetos})

def projeto(request, projeto_slug):
	projeto = Projeto.objects.get(slug=projeto_slug)
	return render(request, 'portal/projetos.html', {'projeto':projeto})

def sobre(request):
	informacoes = Informacao.objects.all()
	funcionarios = Funcionario.objects.all().order_by('nome')
	return render(request, 'portal/sobre.html', {'funcionarios':funcionarios, 'informacoes':informacoes})

def contato(request):
	if request.method == 'POST':
		form = ContatoForm(request.POST)
		if form.is_valid():
			nome = form.cleaned_data['nome']
			email = form.cleaned_data['email']
			telefone = form.cleaned_data['telefone']
			assunto = form.cleaned_data['assunto']
			mensagem = form.cleaned_data['mensagem']
			mensagem_corpo = 'Nome: %s'\
						   	 'Telefone: %s'\
						     'Mensagem: %s' % (nome, telefone, mensagem) 
			if send_mail(assunto, mensagem_corpo, email, [settings.DEFAULT_FROM_EMAIL]):
				messages.success(request, "Mensagem enviada com sucesso")
			else:
				messages.error(request, "Não foi possivel enviar mensagem")
	else:
		form = ContatoForm()
	return render(request, 'portal/contato.html', {'form':form})


def erro404(request):
	return render(request, 'portal/404.html', {})
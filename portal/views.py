from django.shortcuts import render
from .models import Informacao, Funcionario
from blog.models import Noticia

def index(request):
    noticias = Noticia.objects.all().order_by('-data_de_publicacao')[:5]
    return render(request, 'portal/index.html', {'noticias': noticias})

def sobre(request):
    funcionarios = Funcionario.objects.all()
    informacoes = Informacao.objects.all()
    return render(request, 'portal/sobre.html', {'informacoes':informacoes, 'funcionarios':funcionarios})

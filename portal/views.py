from django.shortcuts import render
from blog.models import Noticia

def index(request):
    noticias = Noticia.objects.all().order_by('-data_de_publicacao')[:5]
    return render(request, 'portal/index.html', {'noticias': noticias})

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from .models import Noticia, Categoria

def index(request):
    lista_noticias = Noticia.objects.all().order_by('-data_de_publicacao')
    noticias_mv = Noticia.objects.all().order_by('visualizacoes')[:8]
    paginador = Paginator(lista_noticias, 8)
    pagina = request.GET.get('pagina')
    try:
        noticias = paginador.page(pagina)
    except PageNotAnInteger:
        noticias = paginador.page(1)
    except EmptyPage:
        noticias = paginador.page(paginador.num_pages)
    categorias = Categoria.objects.all().order_by('titulo')
    context = {
        'noticias': noticias,
        'noticias_mv': noticias_mv,
        'categorias': categorias
    }
    return render(request, 'blog/index.html', context)

def categoria(request, categoria_slug):
    categoria = get_object_or_404(Categoria, slug=categoria_slug)
    lista_noticias = Noticia.objects.all().filter(categoria=categoria).order_by('-data_de_publicacao')
    paginador = Paginator(lista_noticias, 8)
    pagina = request.GET.get('pagina')
    try:
        noticias = paginador.page(pagina)
    except PageNotAnInteger:
        noticias = paginador.page(1)
    except EmptyPage:
        noticias = paginador.page(paginador.num_pages)
    categorias = Categoria.objects.all().order_by('titulo')
    context = {
        'categoria': categoria,
        'noticias': noticias, 
        'categorias': categorias
    }
    return render(request, 'blog/categoria.html', context)

def noticia(request, noticia_slug):
    Noticia.objects.filter(slug=noticia_slug).update(visualizacoes=F('visualizacoes') + 1)
    noticia = Noticia.objects.get(slug=noticia_slug)
    context = {
        'noticia': noticia
    }
    return render(request, 'blog/noticia.html', context)


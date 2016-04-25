from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<categoria_slug>[\w-]+)/', views.categoria, name='categoria'),
	url(r'^(?P<noticia_slug>[\w-]+).html$', views.noticia, name='noticia'),
]
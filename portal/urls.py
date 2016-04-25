from django.conf.urls import url, handler404
from . import views

handler404 = 'portal.views.erro404'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^projetos/', views.projetos, name='projetos'),
	url(r'^projetos/(?P<projeto_slug>[\w-]+).html', views.projeto, name='projeto'),
	url(r'^sobre/', views.sobre, name='sobre'),
	url(r'^contato/', views.contato, name='contato'),
]
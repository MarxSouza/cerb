from django.conf.urls import url, handler404
from . import views

handler404 = 'portal.views.erro404'

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
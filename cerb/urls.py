from django.conf.urls import url, include
from django.views.static import serve
from django.contrib import admin
from core import views
from . import settings

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^admin/', admin.site.urls),
    
    url(r'^$', views.home, name='home'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
]

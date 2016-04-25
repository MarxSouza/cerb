from django.conf.urls import url, include
from django.views.static import serve
from django.contrib import admin
from . import settings

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),

    url(r'^admin/', admin.site.urls),
    url(r'', include('portal.urls', namespace='portal')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
]

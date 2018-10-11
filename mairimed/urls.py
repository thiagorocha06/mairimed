from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^administracao/', admin.site.urls),
    #url(r'^accounts/login/$', views.login, name='login'),
    #url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('site_mairimed.urls')),
    url(r'', include('artigos.urls')),
    url(r'', include('usuarios.urls')),
    url(r'^questoes/', include('quiz.urls')),
    url('^', include('django.contrib.auth.urls')),
    url('^contact/', include('contactus.urls')),
    url(r"^chat/", include("chat.urls")),
    url(r'', include('publicacao.urls')),
]

handler404 = 'site_mairimed.views.handler404'
handler500 = 'site_mairimed.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

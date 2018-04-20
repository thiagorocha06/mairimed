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
    url(r'', include('contas.urls')),
    url(r'', include('dicionario_medico.urls')),
    # url(r'', include('dicionario_farmaceutico.urls')),
    url(r'^questoes/', include('quiz.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/login/$', auth_views.LoginView.as_view()),
    url('^', include('django.contrib.auth.urls')),
    url('^contact/', include('contactus.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

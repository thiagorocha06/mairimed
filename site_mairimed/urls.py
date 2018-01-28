from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^mairimed/entrar$', views.EntrarView.as_view(), name='entrar'),
    url(r'^mairimed/sair$', views.EntrarView.as_view(), name='sair'),
    url(r'^mairimed/termos_uso/$', views.termos_uso, name='termos_uso'),
    url(r'^mairimed/sobre/$', views.sobre, name='sobre'),
    url(r'^mairimed/conectado/$', views.ConectadoView.as_view(), name='conectado'),

    url(r'^artigo/administracao/$', views.AdministracaoView.as_view(), name='administracao'),
]

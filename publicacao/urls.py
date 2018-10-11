from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^submit$', views.submit), # submit nova pergunta
    url(r'^deletar_comentario/(?P<pk>\w){0,30}$', views.deletar_comentario, name='deletar_comentario'),
    url(r'^deletar_pergunta/(?P<pk>\w){0,30}$', views.deletar_pergunta, name='deletar_pergunta'),
]

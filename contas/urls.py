from django.conf.urls import url
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)
from . import views

urlpatterns = [
    url(r'^entrar$', views.EntrarView.as_view(), name='entrar'),
    url(r'^sair$', logout, {'template_name': 'contas/logout.html'}, name='logout'),
    # url(r'^login/$', login, {'template_name': 'contas/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'contas/logout.html'}, name='logout'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^perfil/editar$', views.editar_perfil, name='editar_perfil'),
    url(r'^mudar-senha$', views.mudar_senha, name='mudar_senha'),
    url(r'^reset-password$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),

]

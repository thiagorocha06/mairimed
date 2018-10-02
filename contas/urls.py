from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^entrar$', views.entrar, name='entrar'), # login
    url(r'^login$', views.login_view, name='login'), # login
    url(r'^logout$', views.logout_view, name='logout'), # logout
    url(r'^signup$', views.signup), # signup
    
    url(r'^perfil/(?P<pk>\w{0,30})/$', views.perfil_pk, name='detail_user'),

    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^password/$', views.change_password, name='change_password'),

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^del_user/(?P<pk>\w{0,30})/$', views.del_user, name='delete_user'),

    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^mudar-senha$', views.mudar_senha, name='mudar_senha'),
]

from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^termos/(?P<pk>\d+)/$', views.detalhe_termos, name='detalhe_termos'),
    url(r'^termos/lista$', views.lista_termos, name='lista_termos'),

## ALFABETO
    url(r'^termos/termo_a$', views.termo_alfabetico, name='termo_a'),
    url(r'^termos/termo_b$', views.termo_alfabetico, name='termo_b'),
    url(r'^termos/termo_c$', views.termo_alfabetico, name='termo_c'),
    url(r'^termos/termo_d$', views.termo_alfabetico, name='termo_d'),
    url(r'^termos/termo_e$', views.termo_alfabetico, name='termo_e'),
    url(r'^termos/termo_f$', views.termo_alfabetico, name='termo_f'),
    url(r'^termos/termo_g$', views.termo_alfabetico, name='termo_g'),
    url(r'^termos/termo_h$', views.termo_alfabetico, name='termo_h'),
    url(r'^termos/termo_i$', views.termo_alfabetico, name='termo_i'),
    url(r'^termos/termo_j$', views.termo_alfabetico, name='termo_j'),
    url(r'^termos/termo_k$', views.termo_alfabetico, name='termo_k'),
    url(r'^termos/termo_l$', views.termo_alfabetico, name='termo_l'),
    url(r'^termos/termo_m$', views.termo_alfabetico, name='termo_m'),
    url(r'^termos/termo_n$', views.termo_alfabetico, name='termo_n'),
    url(r'^termos/termo_o$', views.termo_alfabetico, name='termo_o'),
    url(r'^termos/termo_p$', views.termo_alfabetico, name='termo_p'),
    url(r'^termos/termo_q$', views.termo_alfabetico, name='termo_q'),
    url(r'^termos/termo_r$', views.termo_alfabetico, name='termo_r'),
    url(r'^termos/termo_s$', views.termo_alfabetico, name='termo_s'),
    url(r'^termos/termo_t$', views.termo_alfabetico, name='termo_t'),
    url(r'^termos/termo_u$', views.termo_alfabetico, name='termo_u'),
    url(r'^termos/termo_v$', views.termo_alfabetico, name='termo_v'),
    url(r'^termos/termo_x$', views.termo_alfabetico, name='termo_x'),
    url(r'^termos/termo_z$', views.termo_alfabetico, name='termo_z'),
]

from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^mairimed/lista_artigos/$', views.lista_artigos, name='lista_artigos'),

### ARTIGOS ###
    url(r'^artigo/cardiologia/$', views.categorias_artigos, name='cardiologia_artigos'),
    url(r'^artigo/cirurgia/$', views.categorias_artigos, name='cirurgia_artigos'),
    url(r'^artigo/dermatologia_artigos/$', views.categorias_artigos, name='dermatologia_artigos'),
    url(r'^artigo/endocrinologia/$', views.categorias_artigos, name='endocrinologia_artigos'),
    url(r'^artigo/gastroenterologia/$', views.categorias_artigos, name='gastroenterologia_artigos'),
    url(r'^artigo/ginecologia/$', views.categorias_artigos, name='ginecologia_artigos'),
    url(r'^artigo/hematologia/$', views.categorias_artigos, name='hematologia_artigos'),
    url(r'^artigo/hepatologia/$', views.categorias_artigos, name='hepatologia_artigos'),
    url(r'^artigo/infectologia/$', views.categorias_artigos, name='infectologia_artigos'),
    url(r'^artigo/med_emergencia_artigos/$', views.categorias_artigos, name='med_emergencia_artigos'),
    url(r'^artigo/nefrologia/$', views.categorias_artigos, name='nefrologia_artigos'),
    url(r'^artigo/neurologia_artigos/$', views.categorias_artigos, name='neurologia_artigos'),
    url(r'^artigo/obstetrícia_artigos/$', views.categorias_artigos, name='obstetrícia_artigos'),
    url(r'^artigo/pediatria/$', views.categorias_artigos, name='pediatria_artigos'),
    url(r'^artigo/pneumologia/$', views.categorias_artigos, name='pneumologia_artigos'),
    url(r'^artigo/reumatologia_artigos/$', views.categorias_artigos, name='reumatologia_artigos'),

    url(r'^artigo/(?P<pk>\d+)/$', views.PostCountHitDetailView.as_view(), name='detalhe_artigo'),

### ESCS ###
    url(r'^escs/3_serie/$', views.categorias_artigos, name='3_serie'),
    url(r'^escs/ha_3/$', views.categorias_artigos, name='ha_3'),
    url(r'^escs/4_serie/$', views.categorias_artigos, name='4_serie'),
    url(r'^escs/ha_4/$', views.categorias_artigos, name='ha_4'),

# 3ª serie - MT
    url(r'^escs/M301/$', views.escs_artigos, name='M301'),
    url(r'^escs/M302/$', views.escs_artigos, name='M302'),
    url(r'^escs/M303/$', views.escs_artigos, name='M303'),
    url(r'^escs/M304/$', views.escs_artigos, name='M304'),
    url(r'^escs/M306/$', views.escs_artigos, name='M306'),
    url(r'^escs/M307/$', views.escs_artigos, name='M307'),
# 3ª serie - HA
    url(r'^escs/ha_ped/$', views.escs_artigos, name='ha_ped'),
    url(r'^escs/ha_abdome/$', views.escs_artigos, name='ha_abdome'),
    url(r'^escs/ha_cm/$', views.escs_artigos, name='ha_cm'),
    url(r'^escs/ha_neurolocom/$', views.escs_artigos, name='ha_neurolocom'),

# 4ª serie - MT
    url(r'^escs/M401/$', views.escs_artigos, name='M401'),
    url(r'^escs/M402/$', views.escs_artigos, name='M402'),
    url(r'^escs/M403/$', views.escs_artigos, name='M403'),
    url(r'^escs/M404/$', views.escs_artigos, name='M404'),
    url(r'^escs/M406/$', views.escs_artigos, name='M406'),
    url(r'^escs/M407/$', views.escs_artigos, name='M407'),

# 4ª serie - HA
    url(r'^escs/ha_ped_emerg/$', views.escs_artigos, name='ha_ped_emerg'),
    url(r'^escs/ha_ped_amb/$', views.escs_artigos, name='ha_ped_amb'),
    url(r'^escs/ha_cm_emerg/$', views.escs_artigos, name='ha_cm_emerg'),
    url(r'^escs/ha_cm_amb/$', views.escs_artigos, name='ha_cm_amb'),
    url(r'^escs/ha_cirurgia/$', views.escs_artigos, name='ha_cirurgia'),
    url(r'^escs/ha_go/$', views.escs_artigos, name='ha_go'),
]

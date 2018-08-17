from django.conf.urls import url
from . import views
from django.urls import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [

    url(r'^artigos/ciclo_clinico/$', view=views.CicloClinicoListaView.as_view(), name='ciclo_clinico'),
    url(r'^ciclo_clinico/(?P<especialidade_name>[\w|\W-]+)/$',
        view=views.ViewCicloClinicoPorEspecialidade.as_view(),
        name='ciclo_clinico_especialidade'),

    url(r'^artigos/ciclo_basico/$', view=views.CicloBasicoListaView.as_view(), name='ciclo_basico'),
    url(r'^ciclo_basico/(?P<temabasico_name>[\w|\W-]+)/$',
        view=views.ViewCicloBasicoPorTema.as_view(),
        name='ciclo_basico_tema'),

    # url(r'^artigos/(?P<slug>[\w-]+)/$', views.PostCountHitDetailView.as_view(), name='detalhe_artigo'),
    url(r'^artigos/(?P<slug>[\w-]+)/$', views.PostCountHitDetailView.as_view(), name='detalhe_artigo'),
    # url(r'^artigo/(?P<pk>\d+)/$', views.RedirecionamentoView.as_view(), name='artigo_detail'),
    url(r'^interno/(?P<pk>\d+)/$', views.PostCountHitDetailView2.as_view(), name='artigo_detail'),

    url(r'^artigo/(?P<pk>\d+)/$', RedirectView.as_view(url='/artigos/ciclo_clinico', permanent=False)),
    url(r'^mairimed/lista_artigos/$', RedirectView.as_view(url='/artigos/ciclo_clinico', permanent=False)),


### ESCS ###
    url(r'^escs/$', views.escs, name='escs'),

# 3ª serie - MT
    url(r'^escs/M301/$', views.escs_artigos, name='M301'),
    url(r'^escs/M302/$', views.escs_artigos, name='M302'),
    url(r'^escs/M303/$', views.escs_artigos, name='M303'),
    url(r'^escs/M304/$', views.escs_artigos, name='M304'),
    url(r'^escs/M306/$', views.escs_artigos, name='M306'),
    url(r'^escs/M307/$', views.escs_artigos, name='M307'),
# 3ª serie - HA
    url(r'^escs/ha_ped_3/$', views.escs_artigos, name='ha_ped_3'),
    url(r'^escs/ha_abdome/$', views.escs_artigos, name='ha_abdome'),
    url(r'^escs/ha_cm_3/$', views.escs_artigos, name='ha_cm_3'),
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

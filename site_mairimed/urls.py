from django.conf.urls import url
from . import views
from .views import chat
from .views import EspecialidadeListaView, ViewArtigosListPorEspecialidade
from links_uteis.views import ViewLinkporInstituicao, ViewLinkporInstituicao2

urlpatterns = [
    url(r'^assistente/$', chat, name='chat'),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^perfil_saude/$', views.perfil_saude, name='perfil_saude'),
    url(r'^perfil_detalhado/$', views.perfil_detalhado, name='perfil_detalhado'),
    url(r'^educacao_medica/$', views.educacaomedicaview, name='educacao_medica'),
    url(r'^mairimed/termos_uso/$', views.termos_uso, name='termos_uso'),
    url(r'^mairimed/sobre/$', views.sobre, name='sobre'),
    url(r'^mairimed/especialidades/$', view=views.EspecialidadeListaView.as_view(), name='especialidades'),
    url(r'^diretrizes/$', ViewLinkporInstituicao.as_view(), name='diretrizes'),
    url(r'^diretrizes_in/$', ViewLinkporInstituicao2.as_view(), name='diretrizes_in'),
    # url(r'^mairimed/especialidades_detalhes$', views.EspecialidadeDetailView.as_view(), name='especialidades_detalhes'),

    url(r'^especialidade/(?P<especialidade_name>[\w|\W-]+)/$',
        view=views.ViewArtigosListPorEspecialidade.as_view(),
        name='especialidade_lista'),

### INTERNO ###
    url(r'^cardiologia/$', views.especialidades, name='cardiologia'),
    url(r'^cirurgia/$', views.especialidades, name='cirurgia'),
    url(r'^dermatologia/$', views.especialidades, name='dermatologia'),
    url(r'^endocrinologia/$', views.especialidades, name='endocrinologia'),
    url(r'^gastroenterologia/$', views.especialidades, name='gastroenterologia'),
    url(r'^ginecologia/$', views.especialidades, name='ginecologia'),
    url(r'^hematologia/$', views.especialidades, name='hematologia'),
    url(r'^hepatologia/$', views.especialidades, name='hepatologia'),
    url(r'^infectologia/$', views.especialidades, name='infectologia'),
    url(r'^med_emergencia_artigos/$', views.especialidades, name='med_emergencia'),
    url(r'^nefrologia/$', views.especialidades, name='nefrologia'),
    url(r'^neurologia/$', views.especialidades, name='neurologia'),
    url(r'^obstetrícia/$', views.especialidades, name='obstetrícia'),
    url(r'^pediatria/$', views.especialidades, name='pediatria'),
    url(r'^pneumologia/$', views.especialidades, name='pneumologia'),
    url(r'^reumatologia/$', views.especialidades, name='reumatologia'),

### Perfil Saude ##
    url(r'^dieta_escolhida$', views.dieta_escolhida, name='dieta_escolhida'),
    url(r'^sintoma_escolhido$', views.sintoma_escolhido, name='sintoma_escolhido'),
]

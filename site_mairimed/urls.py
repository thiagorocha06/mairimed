from django.conf.urls import url
from . import views
from .views import chat, inicio_novo
from .views import EspecialidadeListaView, ViewArtigosListPorEspecialidade, ChatterBotApiView

urlpatterns = [
    url(r'^chat/$', chat, name='chat'),
    url(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
    url(r'^inicio_novo/$', inicio_novo, name='inicio_novo'),
    url(r'^$', views.InicioView.as_view(), name='inicio'),
    url(r'^educacao_medica/$', views.EducacaoMedicaView.as_view(), name='educacao_medica'),
    url(r'^mairimed/termos_uso/$', views.termos_uso, name='termos_uso'),
    url(r'^mairimed/sobre/$', views.sobre, name='sobre'),
    url(r'^mairimed/interno/$', views.ConectadoView.as_view(), name='conectado'),
    url(r'^mairimed/especialidades/$', view=views.EspecialidadeListaView.as_view(), name='especialidades'),
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

    url(r'^artigo/administracao/$', views.AdministracaoView.as_view(), name='administracao'),
]

from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^alimento/(?P<slug>[\w-]+)/$', views.AlimentoDetailView.as_view(), name='detalhe_alimento'),
    url(r'^doenca/(?P<slug>[\w-]+)/$', views.DoencaDetailView.as_view(), name='detalhe_doenca'),
    url(r'^farmaco/(?P<slug>[\w-]+)/$', views.FarmacoDetailView.as_view(), name='detalhe_farmaco'),
    url(r'^termo/(?P<slug>[\w-]+)/$', views.TermoDetailView.as_view(), name='detalhe_termo'),
    url(r'^alimentos/$', views.AlimentosPortalView.as_view(), name='alimentos_portal'),
    url(r'^doencas/$', views.DoencasPortalView.as_view(), name='doenca_portal'),
    url(r'^farmacos/$', views.FarmacosPortalView.as_view(), name='farmacos_portal'),
    url(r'^termos/$', views.TermosPortalView.as_view(), name='termos_portal'),

        url(r'^materias/(?P<slug>[\w-]+)/$', views.MateriaCountHitDetailView.as_view(), name='detalhe_materia'),
        url(r'^condicao/(?P<patologia_name>[\w|\W-]+)/$',
            view=views.ViewMateriaPorPaotologia.as_view(),
            name='patologias_portal'),
]

from django.conf.urls import url
from . import views

urlpatterns = [

        url(r'^materias/(?P<slug>[\w-]+)/$', views.MateriaCountHitDetailView.as_view(), name='detalhe_materia'),
        url(r'^saude/$', views.SaudePortalView.as_view(), name='saude_portal'),
        url(r'^alimentacao/$', views.AlimentacaoPortalView.as_view(), name='alimentacao_portal'),
        url(r'^exercicios/$', views.ExerciciosPortalView.as_view(), name='exercicios_portal'),
        url(r'^bemestar/$', views.BemestarPortalView.as_view(), name='bemestar_portal'),
        url(r'^condicao/(?P<patologia_name>[\w|\W-]+)/$',
            view=views.ViewMateriaPorPaotologia.as_view(),
            name='patologias_portal'),
]

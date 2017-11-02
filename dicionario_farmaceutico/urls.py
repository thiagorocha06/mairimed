from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^farmacos/(?P<pk>\d+)/$', views.detalhe_farmacos, name='detalhe_farmacos'),
    url(r'^farmacos/lista$', views.lista_farmacos, name='lista_farmacos'),

    # CLASSES
    url(r'^farmacos/aine/$', views.classe_farmacos, name='aine_farmacos'),
    url(r'^farmacos/antihipertensivos/$', views.classe_farmacos, name='antihipertensivos_farmacos'),
    url(r'^farmacos/antiagregantes/$', views.classe_farmacos, name='antiagregantes_farmacos'),
    url(r'^farmacos/antianginosos/$', views.classe_farmacos, name='antianginosos_farmacos'),
    url(r'^farmacos/antibioticos/$', views.classe_farmacos, name='antibioticos_farmacos'),
    url(r'^farmacos/anticoagulantes/$', views.classe_farmacos, name='anticoagulantes_farmacos'),
    url(r'^farmacos/hipolipemiantes/$', views.classe_farmacos, name='hipolipemiantes_farmacos'),
]

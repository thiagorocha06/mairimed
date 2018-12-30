from django.conf.urls import url
from . import views
from .views import controles

urlpatterns = [
    url(r'^controles/$', controles, name='controles'),
    url(r'^salvar_peso$', views.salvar_peso,),
    url(r'^salvar_pressao$', views.salvar_pressao,),
    url(r'^salvar_glicemia$', views.salvar_glicemia,),
    url(r'^salvar_temperatura$', views.salvar_temperatura,),
]

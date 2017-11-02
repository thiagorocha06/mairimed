from django.conf.urls import url
from . import views

urlpatterns = [

### EXERCICIOS ###
    url(r'^exercicios/categorias/$', views.categorias_exercicios, name='exercicios_categorias'),
    url(r'^exercicios/ecg/$', views.exercicios_ecg, name='exercicios_ecg'),
    url(r'^exercicios/rx/$', views.exercicios_rx, name='exercicios_rx'),
    url(r'^exercicios/resposta/', views.exercicios_resposta, name='exercicios_resposta'),
]

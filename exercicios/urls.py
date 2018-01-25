from django.conf.urls import url
from . import views

urlpatterns = [

### EXERCICIOS ###
    url(r'^exercicios/categorias_lista/$', views.categorias_lista, name='categorias_lista'),
    url(r'^exercicios/cardiologia/$', views.CategoriasExerciciosView.as_view(), name='cardiologia_exercicios'),
    url(r'^exercicios/cirurgia/$', views.CategoriasExerciciosView.as_view(), name='cirurgia_exercicios'),
    url(r'^exercicios/nefrologia/$', views.CategoriasExerciciosView.as_view(), name='nefrologia_exercicios'),
    url(r'^exercicios/pediatria/$', views.CategoriasExerciciosView.as_view(), name='pediatria_exercicios'),
]

from django.conf.urls import url
from . import views

urlpatterns = [

### EXERCICIOS ###
    url(r'^exercicios/categorias_lista/$', views.categorias_lista, name='categorias_lista'),
    url(r'^exercicios/cardiologia/$', views.categorias_exercicios, name='cardiologia_exercicios'),
]

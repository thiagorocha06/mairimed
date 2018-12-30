from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^novo_treino/$', views.novo_treino, name='novo_treino'),
]

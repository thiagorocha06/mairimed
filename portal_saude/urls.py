from django.conf.urls import url
from . import views

urlpatterns = [

        url(r'^materias/(?P<slug>[\w-]+)/$', views.MateriaCountHitDetailView.as_view(), name='detalhe_materia'),
]

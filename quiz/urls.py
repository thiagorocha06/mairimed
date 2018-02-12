from django.conf.urls import url
from . import views

from .views import QuizListView, SimuladoListView, CategoriesListView,\
    ViewQuizListByEspecialidade, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake, ExercicioIniciado


urlpatterns = [

        url(r'^exercicio$', views.ExercicioListView.as_view(), name='exercicios'),

        url(regex=r'^(?P<quiz_name>[\w-]+)/iniciado/$',
            view=ExercicioIniciado.as_view(),
            name='exercicio_iniciado'),

       url(regex=r'^$',
           view=QuizListView.as_view(),
           name='quiz_index'),

       url(regex=r'^simulados/$',
           view=SimuladoListView.as_view(),
           name='simulado_lista'),

       url(regex=r'^category/$',
           view=CategoriesListView.as_view(),
           name='quiz_category_list_all'),

       url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
           view=ViewQuizListByEspecialidade.as_view(),
           name='quiz_category_list_matching'),

       url(regex=r'^progress/$',
           view=QuizUserProgressView.as_view(),
           name='quiz_progress'),

       url(regex=r'^marking/$',
           view=QuizMarkingList.as_view(),
           name='quiz_marking'),

       url(regex=r'^marking/(?P<pk>[\d.]+)/$',
           view=QuizMarkingDetail.as_view(),
           name='quiz_marking_detail'),

       #  passes variable 'quiz_name' to quiz_take view
       url(regex=r'^(?P<slug>[\w-]+)/$',
           view=QuizDetailView.as_view(),
           name='quiz_start_page'),

       url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
           view=QuizTake.as_view(),
           name='quiz_question'),
]

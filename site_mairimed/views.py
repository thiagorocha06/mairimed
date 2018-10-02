from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from artigos.models import Artigo, Especialidade, Tema
from quiz.models import Quiz, Progress
from django.views.generic import DetailView, TemplateView, ListView, View
from django import forms

from django.http import JsonResponse

def handler404(request):
    return render(request, 'mairimed/404.html')

def handler500(request):
    return render(request, 'mairimed/500.html')

class ArtigoMixinDetailView(object):

    model = Artigo

    def get_context_data(self, **kwargs):
        context = super(ArtigoMixinDetailView, self).get_context_data(**kwargs)
        context['artigo_list'] = Artigo.objects.all().order_by("-titulo")
        return context

# class EducacaoMedicaView(TemplateView):
#     template_name = 'mairimed/conectado.html'
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(ConectadoView, self)\
#             .dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(ConectadoView, self).get_context_data(**kwargs)
#         progress, c = Progress.objects.get_or_create(user=self.request.user)
#
#         context['cat_scores'] = progress.list_all_cat_scores
#         context['exams'] = progress.show_exams()
#         return context

def educacaomedicaview(request):

    if request.user.is_authenticated:
        progress, c = Progress.objects.get_or_create(user=request.user)
        return render(request, 'mairimed/educacao_medica.html', {'cat_scores' : progress.list_all_cat_scores, 'exams' : progress.show_exams()})
    else:
        return render(request, 'mairimed/educacao_medica.html', )

class InicioView(ArtigoMixinDetailView, TemplateView):
    template_name = 'mairimed/inicio.html'

class EspecialidadesDetalhesView(ArtigoMixinDetailView, TemplateView):
    template_name = 'interno_artigos/especialidades_detalhes.html'

    def get_context_data(self, **kwargs):
        context = super(EspecialidadesDetalhesView, self).get_context_data(**kwargs)
        context['artigos'] = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
        return context

def especialidades(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'interno_artigos/especialidades_detalhes.html', {'artigos' : artigos})

class EspecialidadeListaView(ListView):
    model = Especialidade
    # django automaticamente gera: template_name = 'especialidade_list.html'

class ViewArtigosListPorEspecialidade(ListView):
    model = Tema
    template_name = 'artigos/tema_list.html'

    def dispatch(self, request, *args, **kwargs):
        self.especialidade = get_object_or_404(
            Especialidade,
            especialidade=self.kwargs['especialidade_name']
        )

        return super(ViewArtigosListPorEspecialidade, self).\
            dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ViewArtigosListPorEspecialidade, self)\
            .get_context_data(**kwargs)

        context['especialidade'] = self.especialidade
        context['artigo_list'] = Artigo.objects.all().order_by("-data_de_publicacao")
        return context

    def get_queryset(self):
        queryset = super(ViewArtigosListPorEspecialidade, self).get_queryset()
        especialidade_filter = list(queryset.filter(especialidade=self.especialidade).order_by('tema'))
        return especialidade_filter

def termos_uso(request):
    return render(request, 'mairimed/termos_uso.html')

def sobre(request):
    return render(request, 'mairimed/sobre.html')

def chat(request):
    context = {}
    return render(request, 'mairimed/chatbot.html', context)

def diretrizes(request):
    context = {}
    return render(request, 'mairimed/diretrizes.html', context)

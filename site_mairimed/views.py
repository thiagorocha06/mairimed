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
from dicionario_farmaceutico.models import Farmaco
from dicionario_medico.models import Doenca
from portal_saude.models import Materia, Assunto, Patologia
from quiz.models import Quiz, Progress
from django.views.generic import DetailView, TemplateView, ListView
from hitcount.views import HitCountDetailView
from django import forms

def handler404(request):
    return render(request, 'mairimed/404.html')

def handler500(request):
    return render(request, 'mairimed/500.html')

class ArtigoMixinDetailView(object):

    model = Artigo

    def get_context_data(self, **kwargs):
        context = super(ArtigoMixinDetailView, self).get_context_data(**kwargs)
        context['artigo_list'] = Artigo.objects.all().order_by("-hit_count_generic__hits")
        return context

class ConectadoView(TemplateView):
    template_name = 'mairimed/conectado.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ConectadoView, self)\
            .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ConectadoView, self).get_context_data(**kwargs)
        progress, c = Progress.objects.get_or_create(user=self.request.user)

        context['cat_scores'] = progress.list_all_cat_scores
        context['exams'] = progress.show_exams()
        return context

class EducacaoMedicaView(ArtigoMixinDetailView, TemplateView):
    template_name = 'mairimed/educacao_medica.html'

    def get_context_data(self, **kwargs):
        context = super(EducacaoMedicaView, self).get_context_data(**kwargs)

        context['artigos_mais_vistos'] = Artigo.objects.all().order_by("-hit_count_generic__hits")[:5]
        context['ultimos_artigos'] = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('-data_de_publicacao')[:5]
        context['lista_artigos'] = Artigo.objects.all()
        return context

class InicioView(ArtigoMixinDetailView, TemplateView):
    template_name = 'mairimed/inicio.html'

    def get_context_data(self, **kwargs):
        context = super(InicioView, self).get_context_data(**kwargs)
        context['ultimas_materias'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('-data_de_publicacao')[:1]
        context['materia_destaque1'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('-data_de_publicacao')[3]
        context['materia_destaque2'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('-data_de_publicacao')[4]
        context['patologias'] = Patologia.objects.all()
        context['materias'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('-data_de_publicacao')
        context['materia_saude'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[7]).order_by('-data_de_publicacao')[:4]
        context['materia_alimentacao'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[6]).order_by('-data_de_publicacao')[:4]
        context['materia_exercicio'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[1]).order_by('-data_de_publicacao')[:4]
        context['materia_medicamentos'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[5]).order_by('-data_de_publicacao')[:4]
        return context

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

class AdministracaoView(ArtigoMixinDetailView, TemplateView):
    template_name = 'mairimed/administracao_artigo.html'

    def get_context_data(self, **kwargs):
        context = super(AdministracaoView, self).get_context_data(**kwargs)
        lista_artigos = Artigo.objects.all()
        n_artigos = 0
        hits_dia = 0
        hits_semana = 0
        hits_mes = 0
        for artigo in lista_artigos:
            n_artigos = n_artigos + 1
        for artigo in lista_artigos:
            hits_dia = hits_dia + artigo.hit_count.hits_in_last(days=1)
        for artigo in lista_artigos:
            hits_semana = hits_semana + artigo.hit_count.hits_in_last(days=7)
        for artigo in lista_artigos:
            hits_mes = hits_mes + artigo.hit_count.hits_in_last(days=30)
        context['n_artigos'] = n_artigos
        context['hits_dia'] = hits_dia
        context['hits_semana'] = hits_semana
        context['hits_mes'] = hits_mes
        return context

def termos_uso(request):
    return render(request, 'mairimed/termos_uso.html')

def sobre(request):
    return render(request, 'mairimed/sobre.html')

def chat(request):
    context = {}
    return render(request, 'mairimed/chatbot.html', context)

def respond_to_websockets(message):
    lista_farmacos = Farmaco.objects.filter(nome__isnull=False).order_by('nome')
    jokes = {
    'nimesulida': ["""A nimesulida ou nimesulide é um medicamento da classe dos anti-inflamatórios não esteróides (AINEs),
        que atua através da inibição da enzima ciclooxigenase e, consequentemente, da cascata do ácido araquidónico,
         que é responsável pela síntese de substâncias envolvidas na inflamação, tais como as prostaglandinas. Desta forma,
          a nimesulida combate os processos inflamatórios, as dores e a febre."""],
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""]
     }

    result_message = {
        'type': 'text'
    }

    for farmaco in lista_farmacos:
        if farmaco.nome == message['text']:
            result_message['text'] = farmaco.introducao+" Para saber mais sobre "+farmaco.nome+" ou outro fármaco, digite:"+'\n'+"nome e o assunto\
            (indicações, farmacodinâmica, farmacocinética, contraindicações,\
            risco na gravidez, interações ou reações adversas)"
            return result_message
        elif farmaco.nome in message['text'] and "indicações" in message['text']:
            result_message['text'] = "Indicações para "+farmaco.nome+" : "+farmaco.indicacoes
            return result_message
        else:
            pass

    if 'Nimesulida' in message['text'] or 'nimesulida' in message['text']:
        result_message['text'] = random.choice(jokes['nimesulida'])

    elif 'stupid' in message['text']:
        result_message['text'] = random.choice(jokes['stupid'])

    elif 'dumb' in message['text']:
        result_message['text'] = random.choice(jokes['dumb'])

    elif message['text'] in ['oi', 'olá', 'Oi', "Olá"]:
        result_message['text'] = "Olá! Digite um medicamento ou uma doença que você deseja consultar."
    else:
        result_message['text'] = "Não sei uma resposta para essa mensagem. Digite um medicamento ou uma doença que você deseja consultar."

    return result_message

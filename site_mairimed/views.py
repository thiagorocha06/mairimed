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
from dicionario_farmacos.models import Farmaco
from dicionario_doencas.models import Doenca
from dicionario_alimentos.models import Alimento
from dicionario_termos.models import Termo
from portal_saude.models import Materia, Assunto, Patologia
from quiz.models import Quiz, Progress
from django.views.generic import DetailView, TemplateView, ListView, View
from hitcount.views import HitCountDetailView
from django import forms

from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings

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
        context['patologias'] = Patologia.objects.all()
        context['alimentos'] = Alimento.objects.order_by('nome')[:4]
        context['doencas'] = Doenca.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('-data_de_publicacao')[:4]
        context['farmacos'] = Farmaco.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('-data_de_publicacao')[:4]
        context['termos'] = Termo.objects.order_by('nome')[:4]

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

def diretrizes(request):
    context = {}
    return render(request, 'mairimed/diretrizes.html', context)

# CHATBOT

class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def get_conversation(self, request):
        """
        Return the conversation for the session if one exists.
        Create a new conversation if one does not exist.
        """
        from chatterbot.ext.django_chatterbot.models import Conversation, Response

        class Obj(object):
            def __init__(self):
                self.id = None
                self.statements = []

        conversation = Obj()

        conversation.id = request.session.get('conversation_id', 0)
        existing_conversation = False
        try:
            Conversation.objects.get(id=conversation.id)
            existing_conversation = True

        except Conversation.DoesNotExist:
            conversation_id = self.chatterbot.storage.create_conversation()
            request.session['conversation_id'] = conversation_id
            conversation.id = conversation_id

        if existing_conversation:
            responses = Response.objects.filter(
                conversations__id=conversation.id
            )

            for response in responses:
                conversation.statements.append(response.statement.serialize())
                conversation.statements.append(response.response.serialize())

        return conversation

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        # busca o texto digitado pelo usuario
        input_data = json.loads(request.read().decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)
        # busca a conversa extistente ou cria uma nova caso nao exista
        conversation = self.get_conversation(request)
        # busca uma resposta para o texto digitado pelo usuario e retorna um statement
        response = self.chatterbot.get_response(input_data, conversation.id)

        result_message = {
        'type': 'text'
        }
        result_message['text'] = "Assistente Mairimed: "

        # response_data = result_message
        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        conversation = self.get_conversation(request)

        return JsonResponse({
            'name': self.chatterbot.name,
            'conversation': conversation.statements
        })

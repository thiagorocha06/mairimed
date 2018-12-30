import json
import requests
import random

from django import forms
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, TemplateView, ListView, View
from django.http import JsonResponse, Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.utils import timezone

from artigos.models import Artigo, Especialidade, Tema
from quiz.models import Quiz, Progress
from publicacao.models import Pergunta
from publicacao.forms import PerguntaForm
from comentario.models import Comentario
from comentario.forms import ComentarioForm
from controles.models import Pressao, Glicemia, Temperatura, Glicemia, Peso
from usuarios.models import PerfilSaude
from dieta.models import Dieta
from dieta.forms import DietasForm
from sintoma.models import Sintoma
from sintoma.forms import SintomasForm
from usuarios.models import MinhaDieta, MeusSintomas

def handler404(request):
    return render(request, 'mairimed/404.html')

def handler500(request):
    return render(request, 'mairimed/500.html')

def receita(request):
    return render(request, 'recipe.html')

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

def inicio(request):
    if request.user.is_authenticated:
        form = PerguntaForm()
        user = request.user
        perguntas_self = Pergunta.objects.filter(user=user.id).order_by("-pk")
        perguntas_buddies = Pergunta.objects.filter(user__perfilusuario__in=user.perfilusuario.follows.all()).order_by("-pk")
        perguntas = perguntas_self | perguntas_buddies

        content_type = ContentType.objects.get_for_model(Pergunta)
        comentarios = Comentario.objects.filter(content_type=content_type, )

        initial_data = {
                "content_type": content_type,
        }

        comentario_form = ComentarioForm(request.POST or None, initial=initial_data)
        if comentario_form.is_valid():
                c_type = comentario_form.cleaned_data.get("content_type")
                content_type = ContentType.objects.get(model=c_type)
                object_id = request.POST.get("object_id")
                comentario_conteudo = comentario_form.cleaned_data.get("comentario")
                novo_comentario, create = Comentario.objects.get_or_create(
                                        user = request.user,
                                        content_type = content_type,
                                        object_id = object_id,
                                        conteudo = comentario_conteudo
                                        )
                return HttpResponseRedirect('/')

        controles_pressao = Pressao.objects.filter(user=request.user).order_by("-pk")[0:6]
        controles_peso = Peso.objects.filter(user=request.user).order_by("-pk")[0:6]
        controles_temperatura = Temperatura.objects.filter(user=request.user).order_by("-pk")[0:6]
        controles_glicemia = Glicemia.objects.filter(user=request.user).order_by("-pk")[0:6]

        dietas = Dieta.objects.all().order_by("-pk")[0:6]

        context = {
            "comentarios": comentarios,
            'perguntas': perguntas,
            "comentario_form": comentario_form,

            "controles_pressao": controles_pressao,
            "controles_peso": controles_peso,
            "controles_temperatura": controles_temperatura,
            "controles_glicemia": controles_glicemia,

            'dietas': dietas,

            'form': form,
            'user': user,
            'next_url': '/',
        }
        return render(request, 'mairimed/recomendacoes.html', context)
    else:
        return render(request, 'mairimed/inicio.html', )

def perfil_saude(request):
    if request.user.is_authenticated:
        form = PerguntaForm()
        user = request.user
        perguntas_self = Pergunta.objects.filter(user=user.id).order_by("-pk")
        perguntas_buddies = Pergunta.objects.filter(user__perfilusuario__in=user.perfilusuario.follows.all()).order_by("-pk")
        perguntas = perguntas_self | perguntas_buddies

        content_type = ContentType.objects.get_for_model(Pergunta)
        comentarios = Comentario.objects.filter(content_type=content_type, )

        initial_data = {
                "content_type": content_type,
        }

        comentario_form = ComentarioForm(request.POST or None, initial=initial_data)
        if comentario_form.is_valid():
                c_type = comentario_form.cleaned_data.get("content_type")
                content_type = ContentType.objects.get(model=c_type)
                object_id = request.POST.get("object_id")
                comentario_conteudo = comentario_form.cleaned_data.get("comentario")
                novo_comentario, create = Comentario.objects.get_or_create(
                                        user = request.user,
                                        content_type = content_type,
                                        object_id = object_id,
                                        conteudo = comentario_conteudo
                                        )
                return HttpResponseRedirect('/')

        controles_pressao = Pressao.objects.filter(user=request.user).order_by("-pk")[0:6]
        controles_peso = Peso.objects.filter(user=request.user).order_by("-pk")[0:6]
        controles_temperatura = Temperatura.objects.filter(user=request.user).order_by("-pk")[0:6]
        controles_glicemia = Glicemia.objects.filter(user=request.user).order_by("-pk")[0:6]

        dietas = Dieta.objects.all()
        minha_dieta = MinhaDieta.objects.filter(user=request.user)
        dietas_form = DietasForm
        sintomas = Sintoma.objects.all()
        sintomas_form = SintomasForm

        altura = user.perfilsaude.altura
        peso = user.perfilsaude.peso

        context = {
            "comentarios": comentarios,
            'perguntas': perguntas,
            "comentario_form": comentario_form,

            "controles_pressao": controles_pressao,
            "controles_peso": controles_peso,
            "controles_temperatura": controles_temperatura,
            "controles_glicemia": controles_glicemia,

            'form': form,
            'dietas_form': dietas_form,
            'dietas': dietas,
            'minha_dieta': minha_dieta,
            'sintomas_form': sintomas_form,
            'sintomas': sintomas,
            'user': user,
            'next_url': '/',
        }
        return render(request, 'mairimed/perfil_saude.html', context)
    else:
        return render(request, 'mairimed/inicio.html', )

def perfil_detalhado(request):
    if request.user.is_authenticated:
        user = request.user

        minha_dieta = MinhaDieta.objects.filter(user=request.user)

        context = {
            'minha_dieta': minha_dieta,
            'user': user,
            'next_url': '/',
        }
        return render(request, 'mairimed/perfil_detalhado.html', context)
    else:
        return render(request, 'mairimed/inicio.html', )

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

def dieta_escolhida(request):
    user = request.user

    if request.method == "POST":
        form = DietasForm(request.POST)
        if form.is_valid():
            minha_dieta = form.cleaned_data.get('choice')
            nova_dieta, create = MinhaDieta.objects.update_or_create(
                            user = user,
                            defaults={'minha_dieta': minha_dieta}
                            )
    return render(request, 'mairimed/perfil_saude.html')

def sintoma_escolhido(request):
    user = request.user
    if request.method == "POST":
        form = SintomasForm(request.POST)
        if form.is_valid():
            sintoma = form.cleaned_data.get('choice')
            novo_sintoma, create = MeusSintomas.objects.get_or_create(
                            user = user,
                            meus_sintomas = sintoma
                            )
    return render(request, 'mairimed/perfil_saude.html')

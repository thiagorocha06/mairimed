from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from artigos.models import Artigo
from quiz.models import Quiz, Progress
from django.views.generic import DetailView, TemplateView
from hitcount.views import HitCountDetailView
from django import forms

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

# def inicio(request):
#     artigos_mais_vistos = Artigo.objects.all().order_by("-hit_count_generic__hits")[:5]
#     lista_artigos = Artigo.objects.all()
#     conteudo = {
#
#         'artigos_mais_vistos': artigos_mais_vistos,
#         'lista_artigos': lista_artigos
#     }
#     if request.user.is_authenticated():
#         return render(request, 'mairimed/conectado.html', conteudo)
#     else:
#         return render(request, 'mairimed/inicio.html', conteudo)

class InicioView(ArtigoMixinDetailView, TemplateView):
    template_name = 'mairimed/inicio.html'

    def get_context_data(self, **kwargs):
        context = super(InicioView, self).get_context_data(**kwargs)
        context['artigos_mais_vistos'] = Artigo.objects.all().order_by("-hit_count_generic__hits")[:5]
        context['ultimos_artigos'] = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('-data_de_publicacao')[:5]
        context['lista_artigos'] = Artigo.objects.all()
        return context

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

class EntrarView(ArtigoMixinDetailView, TemplateView):
    template_name = 'mairimed/entrar.html'

def termos_uso(request):
    return render(request, 'mairimed/termos_uso.html')

def sobre(request):
    return render(request, 'mairimed/sobre.html')

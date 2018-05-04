from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Artigo
from contas.models import Estudante
from .forms import ArtigoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, TemplateView, ListView
from hitcount.views import HitCountDetailView
from artigos.models import Artigo, Especialidade, Tema, TemaBasico

class ArtigoMixinDetailView(object):

    model = Artigo

    def get_context_data(self, **kwargs):
        context = super(ArtigoMixinDetailView, self).get_context_data(**kwargs)
        context['artigo_list'] = Artigo.objects.all().order_by("-hit_count_generic__hits")
        return context

class PostCountHitDetailView(ArtigoMixinDetailView, HitCountDetailView):
    """
    Generic hitcount class based view that will also perform the hitcount logic.
    """
    count_hit = False
    template_name = 'artigos/detalhe_artigo.html'
    slug_field = 'url'

class PostCountHitDetailView2(ArtigoMixinDetailView, HitCountDetailView):
    """
    Generic hitcount class based view that will also perform the hitcount logic.
    """
    count_hit = True
    template_name = 'artigos/artigo_detail.html'

def lista_artigos(request):
    estudante = Estudante.objects
    lista_artigos = Artigo.objects.filter(
                    data_de_publicacao__lte=timezone.now(),
                    artigo_interno=False
                    ).order_by('-hit_count_generic__hits')

    #Pesquisa
    termo_pesquisa = request.GET.get("campo_pesquisa")
    if termo_pesquisa:
        lista_artigos = lista_artigos.filter(titulo__icontains=termo_pesquisa)

    #Paginacao
    paginator = Paginator(lista_artigos, 10) # Show 10 contacts per page
    page_request_var = "pagina"
    page = request.GET.get(page_request_var)
    try:
        artigos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        artigos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        artigos = paginator.page(paginator.num_pages)

    conteudo = {
        'lista_artigos': artigos,
        'estudante': estudante,
        'page_request_var': page_request_var
    }

    return render(request, 'artigos/lista_artigos.html', conteudo)

def categorias_artigos(request):
    artigos = Artigo.objects.filter(
                    data_de_publicacao__lte=timezone.now(),
                    artigo_interno=False
                    ).order_by('data_de_publicacao')
    return render(request, 'artigos/escs_modulos.html', {'artigos' : artigos})

def escs_artigos(request):
    artigos = Artigo.objects.filter(
                    data_de_publicacao__lte=timezone.now(),
                    artigo_interno=False
                    ).order_by('data_de_publicacao')
    return render(request, 'artigos/escs_artigos.html', {'artigos' : artigos})

class CicloClinicoListaView(ListView):
    template_name = 'artigos/cicloclinico_esp.html'
    model = Especialidade

class ViewCicloClinicoPorEspecialidade(ListView):
    model = Tema
    template_name = 'artigos/cicloclinico_temas.html'

    def dispatch(self, request, *args, **kwargs):
        self.especialidade = get_object_or_404(
            Especialidade,
            especialidade=self.kwargs['especialidade_name']
        )

        return super(ViewCicloClinicoPorEspecialidade, self).\
            dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ViewCicloClinicoPorEspecialidade, self)\
            .get_context_data(**kwargs)

        context['especialidade'] = self.especialidade
        context['artigo_list'] = Artigo.objects.all().order_by("-data_de_publicacao")
        return context

    def get_queryset(self):
        queryset = super(ViewCicloClinicoPorEspecialidade, self).get_queryset()
        especialidade_filter = list(queryset.filter(especialidade=self.especialidade).order_by('tema'))
        return especialidade_filter

class CicloBasicoListaView(ListView):
    template_name = 'artigos/ciclobasico_tema.html'
    model = TemaBasico

class ViewCicloBasicoPorTema(ListView):
    model = Artigo
    template_name = 'artigos/ciclobasico_artigos.html'

    def dispatch(self, request, *args, **kwargs):
        self.tema_basico = get_object_or_404(
            TemaBasico,
            tema_basico=self.kwargs['temabasico_name']
        )

        return super(ViewCicloBasicoPorTema, self).\
            dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ViewCicloBasicoPorTema, self)\
            .get_context_data(**kwargs)

        context['temabasico'] = self.tema_basico
        context['artigo_list'] = Artigo.objects.all().order_by("-data_de_publicacao")
        return context

def detalhe_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    estudante = Estudante.objects
    return render(request, 'artigos/detalhe_artigo.html', {'estudante': estudante, 'artigo': artigo})

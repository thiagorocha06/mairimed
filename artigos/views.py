from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Artigo
from contas.models import Estudante
from .forms import ArtigoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, TemplateView
from hitcount.views import HitCountDetailView

class ArtigoMixinDetailView(object):
    """
    Mixin to same us some typing.  Adds context for us!
    """
    model = Artigo

    def get_context_data(self, **kwargs):
        context = super(ArtigoMixinDetailView, self).get_context_data(**kwargs)
        context['artigo_list'] = Artigo.objects.all()[:5]
        return context

class PostCountHitDetailView(ArtigoMixinDetailView, HitCountDetailView):
    """
    Generic hitcount class based view that will also perform the hitcount logic.
    """
    count_hit = True
    template_name = 'artigos/detalhe_artigo.html'

def inicio(request):
    estudante = Estudante.objects
    lista_artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('-data_de_publicacao')

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

    return render(request, 'mairimed/inicio.html', conteudo)

def termos_uso(request):
    return render(request, 'mairimed/termos_uso.html')

def sobre(request):
    return render(request, 'mairimed/sobre.html')

def bootstrap(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    return render(request, 'mairimed/bootstrap.html', {'artigo': artigo})

def categorias_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias_artigos.html', {'artigos' : artigos})

def escs_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/escs_artigos.html', {'artigos' : artigos})

### ARTIGOS ###

def infectologia_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/infectologia_artigos.html', {'artigos' : artigos})

def cardiologia_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/cardiologia_artigos.html', {'artigos' : artigos})

def endocrinologia_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/endocrinologia_artigos.html', {'artigos' : artigos})

def nefrologia_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/nefrologia_artigos.html', {'artigos' : artigos})

def pediatria_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/pediatria_artigos.html', {'artigos' : artigos})

def pneumologia_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/pneumologia_artigos.html', {'artigos' : artigos})

def detalhe_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    estudante = Estudante.objects
    return render(request, 'artigos/detalhe_artigo.html', {'estudante': estudante, 'artigo': artigo})

def favoritos_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    artigos_favoritos = Estudante.artigos_favoritos
    estudante = Estudante.objects
    estudante.artigos_favoritos.add(artigo)
    return redirect('detalhe_artigo', pk=pk)

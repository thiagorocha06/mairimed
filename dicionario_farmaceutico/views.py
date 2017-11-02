from django.shortcuts import render, get_object_or_404, redirect
from .models import Farmaco
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def lista_farmacos(request):
    lista_farmacos = Farmaco.objects.filter(nome__isnull=False).order_by('nome')

    #Pesquisa
    termo_pesquisa = request.GET.get("campo_pesquisa")
    if termo_pesquisa:
        lista_farmacos = lista_farmacos.filter(nome__icontains=termo_pesquisa)

    #Paginacao
    paginator = Paginator(lista_farmacos, 25) # Show 5 contacts per page
    page_request_var = "pagina"
    page = request.GET.get(page_request_var)
    try:
        farmacos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        farmacos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        farmacos = paginator.page(paginator.num_pages)

    conteudo = {
        'farmacos' : farmacos,
        'page_request_var': page_request_var,
    }

    return render(request, 'farmacos/lista_farmacos.html', conteudo)

def detalhe_farmacos(request, pk):
    farmaco = get_object_or_404(Farmaco, pk=pk)
    return render(request, 'farmacos/detalhe_farmacos.html', {'farmaco': farmaco})

def classe_farmacos(request):
    farmacos = Farmaco.objects.filter(nome__isnull=False).order_by('nome')
    return render(request, 'farmacos/classe_farmacos.html', {'farmacos' : farmacos})

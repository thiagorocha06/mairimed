from django.shortcuts import render, get_object_or_404, redirect
from .models import Termo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import resolve

def lista_termos(request):
    lista_termos = Termo.objects.filter(definicao__isnull=False).order_by('nome')

    #Pesquisa
    termo_pesquisa = request.GET.get("campo_pesquisa")
    if termo_pesquisa:
        lista_termos = lista_termos.filter(nome__icontains=termo_pesquisa)

    #Paginacao
    paginator = Paginator(lista_termos, 25) # Show 5 contacts per page
    page_request_var = "pagina"
    page = request.GET.get(page_request_var)
    try:
        termos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        termos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        termos = paginator.page(paginator.num_pages)

    conteudo = {
        'termos' : termos,
        'page_request_var': page_request_var
    }

    return render(request, 'termos/lista_termos.html', conteudo)

def detalhe_termos(request, pk):
    termo = get_object_or_404(Termo, pk=pk)
    return render(request, 'termos/detalhe_termos.html', {'termo': termo})


### ALFABETO ###

def termo_alfabetico(request):
    current_url = resolve(request.path_info).url_name
    if current_url == 'termo_a':
        letra = "A"
    if current_url == 'termo_b':
        letra = "B"
    if current_url == 'termo_c':
        letra = "C"
    if current_url == 'termo_d':
        letra = "D"
    if current_url == 'termo_e':
        letra = "E"
    if current_url == 'termo_f':
        letra = "F"
    if current_url == 'termo_g':
        letra = "G"
    if current_url == 'termo_h':
        letra = "H"
    if current_url == 'termo_i':
        letra = "I"
    if current_url == 'termo_j':
        letra = "J"
    if current_url == 'termo_k':
        letra = "K"
    if current_url == 'termo_l':
        letra = "L"
    if current_url == 'termo_m':
        letra = "M"
    if current_url == 'termo_n':
        letra = "N"
    if current_url == 'termo_o':
        letra = "O"
    if current_url == 'termo_p':
        letra = "P"
    if current_url == 'termo_q':
        letra = "Q"
    if current_url == 'termo_r':
        letra = "R"
    if current_url == 'termo_s':
        letra = "S"
    if current_url == 'termo_t':
        letra = "T"
    if current_url == 'termo_u':
        letra = "U"
    if current_url == 'termo_v':
        letra = "V"
    if current_url == 'termo_x':
        letra = "X"
    if current_url == 'termo_z':
        letra = "Z"
    lista_termos = Termo.objects.filter(definicao__isnull=False).order_by('nome')
    lista_termos_a = lista_termos.filter(nome__istartswith=letra).order_by('nome')

    #Pesquisa
    termo_pesquisa = request.GET.get("campo_pesquisa")
    if termo_pesquisa:
        lista_termos = lista_termos.filter(nome__icontains=termo_pesquisa)
        lista_termos_a = lista_termos
        letra = ""

    #Paginacao
    paginator = Paginator(lista_termos_a, 25) # Show 5 contacts per page
    page_request_var = "pagina"
    page = request.GET.get(page_request_var)
    try:
        termos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        termos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        termos = paginator.page(paginator.num_pages)

    conteudo = {
        'termos' : termos,
        'page_request_var': page_request_var,
        'letra' : letra
    }

    return render(request, 'termos/termo_alfabetico.html', conteudo)

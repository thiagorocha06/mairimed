from django.shortcuts import render
from .models import Exercicio

### EXERCICIOS ###

def categorias_exercicios(request):
    return render(request, 'exercicios/categorias_exercicios.html')

def exercicios_ecg(request):
    exercicios = Exercicio.objects.filter(nome__isnull=False).order_by("pk")
    return render(request, 'exercicios/exercicios_ecg.html', {'exercicios' : exercicios})

def exercicios_rx(request):
    return render(request, 'exercicios/exercicios_rx.html')

def exercicios_resposta(request):
    exercicios = Exercicio.objects.filter(nome__isnull=False).order_by('pk')
    #exercicio_resposta = get_object_or_404(Exercicio, pk=pk)
    return render(request, 'exercicios/exercicios_resposta.html', {'exercicios' : exercicios})
    #return redirect(request.META['HTTP_REFERER'])
    #return redirect(instance.get_absolute_url())

#def exercicios_resposta(request):
#    exercicios = Exercicio.objects.filter(nome__isnull=False).order_by('pk')
#    mostrar_r = False
#    if request.GET.get("mostrar_resposta"):
#        mostrar_r = True
    #exercicio_resposta = get_object_or_404(Exercicio, pk=pk)
#    return render(request, 'exercicios/exercicios_ecg.html', {'exercicios' : exercicios, 'mostrar_r' : mostrar_r})

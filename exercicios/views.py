from django.shortcuts import render
from .models import Exercicio
from django.db.models import Q
from django.views.generic import DetailView, TemplateView
from django.db.models.aggregates import Count
from random import randint

### EXERCICIOS ###

def categorias_lista(request):
    return render(request, 'exercicios/categorias_lista.html')

class SimuladoExerciciosView(TemplateView):
    template_name = 'exercicios/simulado_exercicios.html'

    def get_context_data(self, **kwargs):
        context = super(SimuladoExerciciosView, self).get_context_data(**kwargs)
        exercicios = Exercicio.objects.filter(data_de_criacao__isnull=False).order_by("pk")
        query = self.request.GET.get('localidade')
        SES_DF_2018 = []
        SES_DF_2017 = []
        for exercicio in exercicios:
            if exercicio.simulado == "SES DF 2018":
                SES_DF_2018.append(exercicio)
            elif exercicio.simulado == "SES DF 2017":
                SES_DF_2017.append(exercicio)
        context['SES_DF_2018'] = SES_DF_2018
        context['SES_DF_2017'] = SES_DF_2017
        context['exercicios'] = exercicios
        return context

class CategoriasExerciciosView(TemplateView):
    template_name = 'exercicios/categorias_exercicios.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriasExerciciosView, self).get_context_data(**kwargs)
        queryset_list = Exercicio.objects.filter(data_de_criacao__isnull=False).order_by("pk")
        query = self.request.GET.get('localidade')
        if query:
            queryset_list = queryset_list.filter(
                Q(localidade__icontains=query)
            ).distinct()
        context['exercicios'] = queryset_list
        return context

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

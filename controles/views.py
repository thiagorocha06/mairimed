from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponse

from controles.forms import PressaoForm, TemperaturaForm, PesoForm, GlicemiaForm
from controles.models import Pressao, Glicemia, Temperatura, Glicemia, Peso

@login_required
def controles(request):
    user = request.user
    pressao_form = PressaoForm
    temperatura_form = TemperaturaForm
    peso_form = PesoForm
    glicemia_form = GlicemiaForm

    context = {
        'pressao_form': pressao_form,
        'temperatura_form': temperatura_form,
        'peso_form': peso_form,
        'glicemia_form': glicemia_form,
    }

    return render(request, 'controles/controles.html', context)

@login_required
def salvar_pressao(request):
    user = request.user
    pressao_form = PressaoForm(request.POST)
    temperatura_form = TemperaturaForm(request.POST)
    peso_form = PesoForm(request.POST)
    glicemia_form = GlicemiaForm(request.POST)

    if pressao_form.is_valid():
            sistolica = pressao_form.cleaned_data.get("sistolica")
            diastolica = pressao_form.cleaned_data.get("diastolica")
            data = pressao_form.cleaned_data.get("data")
            hora = pressao_form.cleaned_data.get("hora")
            nova_pressao, create = Pressao.objects.get_or_create(
                                    user = request.user,
                                    sistolica = sistolica,
                                    diastolica = diastolica,
                                    data = data,
                                    hora = hora,
                                    )
            return HttpResponseRedirect('/')

    context = {
        'pressao_form': pressao_form,
        'temperatura_form': temperatura_form,
        'peso_form': peso_form,
        'glicemia_form': glicemia_form,
    }

    return render(request, 'controles/controles.html', context)

@login_required
def salvar_peso(request):
    user = request.user
    pressao_form = PressaoForm(request.POST)
    temperatura_form = TemperaturaForm(request.POST)
    peso_form = PesoForm(request.POST)
    glicemia_form = GlicemiaForm(request.POST)

    if peso_form.is_valid():
            peso = peso_form.cleaned_data.get("peso")
            data = peso_form.cleaned_data.get("data")
            hora = peso_form.cleaned_data.get("hora")
            novo_peso, create = Peso.objects.get_or_create(
                                    user = request.user,
                                    peso = peso,
                                    data = data,
                                    hora = hora,
                                    )
            return HttpResponseRedirect('/')

    context = {
        'pressao_form': pressao_form,
        'temperatura_form': temperatura_form,
        'peso_form': peso_form,
        'glicemia_form': glicemia_form,
    }

    return render(request, 'controles/controles.html', context)

@login_required
def salvar_glicemia(request):
    user = request.user
    pressao_form = PressaoForm(request.POST)
    temperatura_form = TemperaturaForm(request.POST)
    peso_form = PesoForm(request.POST)
    glicemia_form = GlicemiaForm(request.POST)

    if glicemia_form.is_valid():
            glicemia = glicemia_form.cleaned_data.get("glicemia")
            data = glicemia_form.cleaned_data.get("data")
            hora = glicemia_form.cleaned_data.get("hora")
            nova_glicemia, create = Glicemia.objects.get_or_create(
                                    user = request.user,
                                    glicemia = glicemia,
                                    data = data,
                                    hora = hora,
                                    )
            return HttpResponseRedirect('/')

    context = {
        'pressao_form': pressao_form,
        'temperatura_form': temperatura_form,
        'peso_form': peso_form,
        'glicemia_form': glicemia_form,
    }

    return render(request, 'controles/controles.html', context)

@login_required
def salvar_temperatura(request):
    user = request.user
    pressao_form = PressaoForm(request.POST)
    temperatura_form = TemperaturaForm(request.POST)
    peso_form = PesoForm(request.POST)
    glicemia_form = GlicemiaForm(request.POST)

    if temperatura_form.is_valid():
            temperatura = temperatura_form.cleaned_data.get("temperatura")
            data = temperatura_form.cleaned_data.get("data")
            hora = temperatura_form.cleaned_data.get("hora")
            nova_temperatura, create = Temperatura.objects.get_or_create(
                                    user = request.user,
                                    temperatura = temperatura,
                                    data = data,
                                    hora = hora,
                                    )
            return HttpResponseRedirect('/')

    context = {
        'pressao_form': pressao_form,
        'temperatura_form': temperatura_form,
        'peso_form': peso_form,
        'glicemia_form': glicemia_form,
    }

    return render(request, 'controles/controles.html', context)

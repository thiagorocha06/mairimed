from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404, HttpResponseRedirect, HttpResponse
from django.db.models import Q

from dieta.forms import NovaDietaForm, AlimentoForm
from dieta.models import Dieta, Alimento, SegDesjejum, SegAlmoco, SegJantar, SegLanches, TerDesjejum, TerAlmoco, TerJantar, TerLanches, QuaDesjejum, QuaAlmoco, QuaJantar, QuaLanches, QuiDesjejum, QuiAlmoco, QuiJantar, QuiLanches, SexDesjejum, SexAlmoco, SexJantar, SexLanches, SabDesjejum, SabAlmoco, SabJantar, SabLanches, DomDesjejum, DomAlmoco, DomJantar, DomLanches
from usuarios.models import MinhaDieta

@login_required
def nova_dieta(request):
    form = NovaDietaForm
    dietas = Dieta.objects.filter(user=request.user)

    context = {
        'form': form,
        'dietas': dietas,
    }

    return render(request, 'dieta/nova_dieta.html', context)

def deletar_dieta(request, pk):
    form = NovaDietaForm
    dietas = Dieta.objects.filter(user=request.user)
    dieta = Dieta.objects.get(pk=pk)

    if request.method == "POST":
        dieta.delete()
        messages.success(request, 'Dieta apagada')

        context = {
            'form': form,
            'dietas': dietas,
        }

        return render(request, 'dieta/nova_dieta.html', context)

    context = {
        'form': form,
        'dietas': dietas,
    }

    return render(request, 'dieta/editar_dieta.html', context)

def salvar_dieta(request):
    user = request.user
    form = NovaDietaForm(request.POST or None)
    alimentos = Alimento.objects.all()

    if form.is_valid():
        nome_dieta = form.cleaned_data.get("nome_dieta")
        descricao = form.cleaned_data.get("descricao")

        nova_dieta, create = Dieta.objects.get_or_create(
                    user=user,
                    nome_dieta=nome_dieta,
                    descricao=descricao
                    )

        context = {
            'dieta': nova_dieta,
            'alimentos': alimentos,
        }

        return render(request, 'dieta/editar_dieta.html', context)

    context = {
        'form': form,
        'desjejum_form': desjejum_form,
    }

    return render(request, 'dieta/editar_dieta.html', context)

def editar_dieta(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        desjejum = SegDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'desjejum': desjejum
        }

        return render(request, 'dieta/editar_dieta.html', context)

    context= {}

    return render(request, 'dieta/editar_dieta.html', context)

def lista_dietas(request):
    user = request.user
    dietas = Dieta.objects.all()

    context = {
        'dietas': dietas,
    }

    return render(request, 'dieta/lista_dietas.html', context)

def detalhe_dieta(request, pk):
    minha_dieta = get_object_or_404(MinhaDieta, user=request.user)
    dieta = get_object_or_404(Dieta, pk=pk)
    desjejum = SegDesjejum.objects.filter(dieta=dieta.id)

    context = {
        'dieta': dieta,
        'desjejum': desjejum,
        'minha_dieta': minha_dieta,
    }

    return render(request, 'dieta/detalhe_dieta.html', context)

def dieta_selecionada(request, pk):
    user = request.user
    minha_dieta = get_object_or_404(Dieta, pk=pk)
    dietas = Dietas.objects.all()

    if request.method == "POST":
            nova_dieta, create = MinhaDieta.objects.update_or_create(
                            user = user,
                            defaults={'minha_dieta': minha_dieta}
                            )
            minha_dieta = nova_dieta

    context = {
        'minha_dieta': minha_dieta,
        'dietas': dietas
    }

    return HttpResponseRedirect('/perfil_saude', context)

###################
#### REFEICOES ####
###################

#### SEGUNDA ####

def seg_desjejum(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SegDesjejum.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/seg_desjejum.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/seg_desjejum.html', context)

def add_desjejum_seg(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SegDesjejum.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SegDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/seg_desjejum/'+pk, context)

    return render(request, 'dieta/seg_desjejum.html')

def del_desjejum_seg(request, pk):
    alimentos = Alimento.objects.all()
    obj = SegDesjejum.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SegDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/seg_desjejum/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/seg_desjejum.html', context)

def seg_almoco(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SegAlmoco.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/seg_almoco.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/seg_almoco.html', context)

def add_almoco_seg(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SegAlmoco.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SegAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/seg_almoco/'+pk, context)

    return render(request, 'dieta/seg_almoco.html')

def del_almoco_seg(request, pk):
    alimentos = Alimento.objects.all()
    obj = SegAlmoco.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SegAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/seg_almoco/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/seg_almoco.html', context)

def seg_jantar(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SegJantar.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/seg_jantar.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/seg_jantar.html', context)

def add_jantar_seg(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SegJantar.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SegJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/seg_jantar/'+pk, context)

    return render(request, 'dieta/seg_jantar.html')

def del_jantar_seg(request, pk):
    alimentos = Alimento.objects.all()
    obj = SegJantar.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SegJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/seg_jantar/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/seg_jantar.html', context)

def seg_lanches(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SegLanches.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/seg_lanches.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/seg_lanches.html', context)

def add_lanches_seg(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SegLanches.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SegLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/seg_lanches/'+pk, context)

    return render(request, 'dieta/seg_lanches.html')

def del_lanches_seg(request, pk):
    alimentos = Alimento.objects.all()
    obj = SegLanches.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SegLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/seg_lanches/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/seg_lanches.html', context)

#### TERCA ####

def ter_desjejum(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = TerDesjejum.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/ter_desjejum.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/ter_desjejum.html', context)

def add_desjejum_ter(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = TerDesjejum.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = TerDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/ter_desjejum/'+pk, context)

    return render(request, 'dieta/ter_desjejum.html')

def del_desjejum_ter(request, pk):
    alimentos = Alimento.objects.all()
    obj = TerDesjejum.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = TerDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/ter_desjejum/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/ter_desjejum.html', context)

def ter_almoco(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = TerAlmoco.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/ter_almoco.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/ter_almoco.html', context)

def add_almoco_ter(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = TerAlmoco.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = TerAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/ter_almoco/'+pk, context)

    return render(request, 'dieta/ter_almoco.html')

def del_almoco_ter(request, pk):
    alimentos = Alimento.objects.all()
    obj = TerAlmoco.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = TerAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/ter_almoco/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/ter_almoco.html', context)

def ter_jantar(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = TerJantar.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/ter_jantar.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/ter_jantar.html', context)

def add_jantar_ter(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = TerJantar.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = TerJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/ter_jantar/'+pk, context)

    return render(request, 'dieta/ter_jantar.html')

def del_jantar_ter(request, pk):
    alimentos = Alimento.objects.all()
    obj = TerJantar.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = TerJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/ter_jantar/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/ter_jantar.html', context)

def ter_lanches(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = TerLanches.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/ter_lanches.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/ter_lanches.html', context)

def add_lanches_ter(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = TerLanches.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = TerLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/ter_lanches/'+pk, context)

    return render(request, 'dieta/ter_lanches.html')

def del_lanches_ter(request, pk):
    alimentos = Alimento.objects.all()
    obj = TerLanches.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = TerLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/ter_lanches/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/ter_lanches.html', context)

#### QUARTA ####

def qua_desjejum(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = QuaDesjejum.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/qua_desjejum.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/qua_desjejum.html', context)

def add_desjejum_qua(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = QuaDesjejum.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = QuaDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qua_desjejum/'+pk, context)

    return render(request, 'dieta/qua_desjejum.html')

def del_desjejum_qua(request, pk):
    alimentos = Alimento.objects.all()
    obj = QuaDesjejum.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = QuaDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qua_desjejum/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/qua_desjejum.html', context)

def qua_almoco(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = QuaAlmoco.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/qua_almoco.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/qua_almoco.html', context)

def add_almoco_qua(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = QuaAlmoco.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = QuaAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qua_almoco/'+pk, context)

    return render(request, 'dieta/qua_almoco.html')

def del_almoco_qua(request, pk):
    alimentos = Alimento.objects.all()
    obj = QuaAlmoco.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = QuaAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qua_almoco/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/qua_almoco.html', context)

def qua_jantar(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = QuaJantar.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/qua_jantar.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/qua_jantar.html', context)

def add_jantar_qua(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = QuaJantar.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = QuaJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qua_jantar/'+pk, context)

    return render(request, 'dieta/qua_jantar.html')

def del_jantar_qua(request, pk):
    alimentos = Alimento.objects.all()
    obj = QuaJantar.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = QuaJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qua_jantar/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/qua_jantar.html', context)

def qua_lanches(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = QuaLanches.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/qua_lanches.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/qua_lanches.html', context)

def add_lanches_qua(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = QuaLanches.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = QuaLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qua_lanches/'+pk, context)

    return render(request, 'dieta/qua_lanches.html')

def del_lanches_qua(request, pk):
    alimentos = Alimento.objects.all()
    obj = QuaLanches.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = QuaLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qua_lanches/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/qua_lanches.html', context)

#### QUINTA ####

def qui_desjejum(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = QuiDesjejum.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/qui_desjejum.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/qui_desjejum.html', context)

def add_desjejum_qui(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = QuiDesjejum.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = QuiDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qui_desjejum/'+pk, context)

    return render(request, 'dieta/qui_desjejum.html')

def del_desjejum_qui(request, pk):
    alimentos = Alimento.objects.all()
    obj = QuiDesjejum.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = QuiDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qui_desjejum/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/qui_desjejum.html', context)

def qui_almoco(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = QuiAlmoco.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/qui_almoco.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/qui_almoco.html', context)

def add_almoco_qui(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = QuiAlmoco.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = QuiAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qui_almoco/'+pk, context)

    return render(request, 'dieta/qui_almoco.html')

def del_almoco_qui(request, pk):
    alimentos = Alimento.objects.all()
    obj = QuiAlmoco.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = QuiAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qui_almoco/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/qui_almoco.html', context)

def qui_jantar(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = QuiJantar.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/qui_jantar.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/qui_jantar.html', context)

def add_jantar_qui(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = QuiJantar.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = QuiJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qui_jantar/'+pk, context)

    return render(request, 'dieta/qui_jantar.html')

def del_jantar_qui(request, pk):
    alimentos = Alimento.objects.all()
    obj = QuiJantar.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = QuiJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qui_jantar/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/qui_jantar.html', context)

def qui_lanches(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = QuiLanches.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/qui_lanches.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/qui_lanches.html', context)

def add_lanches_qui(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = QuiLanches.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = QuiLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qui_lanches/'+pk, context)

    return render(request, 'dieta/qui_lanches.html')

def del_lanches_qui(request, pk):
    alimentos = Alimento.objects.all()
    obj = QuiLanches.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = QuiLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/qui_lanches/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/qui_lanches.html', context)

#### SEXTA ####

def sex_desjejum(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SexDesjejum.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/sex_desjejum.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/sex_desjejum.html', context)

def add_desjejum_sex(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SexDesjejum.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SexDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sex_desjejum/'+pk, context)

    return render(request, 'dieta/sex_desjejum.html')

def del_desjejum_sex(request, pk):
    alimentos = Alimento.objects.all()
    obj = SexDesjejum.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SexDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sex_desjejum/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/sex_desjejum.html', context)

def sex_almoco(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SexAlmoco.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/sex_almoco.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/sex_almoco.html', context)

def add_almoco_sex(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SexAlmoco.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SexAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sex_almoco/'+pk, context)

    return render(request, 'dieta/sex_almoco.html')

def del_almoco_sex(request, pk):
    alimentos = Alimento.objects.all()
    obj = SexAlmoco.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SexAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sex_almoco/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/sex_almoco.html', context)

def sex_jantar(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SexJantar.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/sex_jantar.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/sex_jantar.html', context)

def add_jantar_sex(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SexJantar.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SexJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sex_jantar/'+pk, context)

    return render(request, 'dieta/sex_jantar.html')

def del_jantar_sex(request, pk):
    alimentos = Alimento.objects.all()
    obj = SexJantar.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SexJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sex_jantar/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/sex_jantar.html', context)

def sex_lanches(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SexLanches.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/sex_lanches.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/sex_lanches.html', context)

def add_lanches_sex(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SexLanches.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SexLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sex_lanches/'+pk, context)

    return render(request, 'dieta/sex_lanches.html')

def del_lanches_sex(request, pk):
    alimentos = Alimento.objects.all()
    obj = SexLanches.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SexLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sex_lanches/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/sex_lanches.html', context)

#### SABADO ####

def sab_desjejum(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SabDesjejum.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/sab_desjejum.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/sab_desjejum.html', context)

def add_desjejum_sab(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SabDesjejum.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SabDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sab_desjejum/'+pk, context)

    return render(request, 'dieta/sab_desjejum.html')

def del_desjejum_sab(request, pk):
    alimentos = Alimento.objects.all()
    obj = SabDesjejum.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SabDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sab_desjejum/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/sab_desjejum.html', context)

def sab_almoco(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SabAlmoco.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/sab_almoco.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/sab_almoco.html', context)

def add_almoco_sab(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SabAlmoco.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SabAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sab_almoco/'+pk, context)

    return render(request, 'dieta/sab_almoco.html')

def del_almoco_sab(request, pk):
    alimentos = Alimento.objects.all()
    obj = SabAlmoco.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SabAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sab_almoco/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/sab_almoco.html', context)

def sab_jantar(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SabJantar.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/sab_jantar.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/sab_jantar.html', context)

def add_jantar_sab(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SabJantar.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SabJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sab_jantar/'+pk, context)

    return render(request, 'dieta/sab_jantar.html')

def del_jantar_sab(request, pk):
    alimentos = Alimento.objects.all()
    obj = SabJantar.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SabJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sab_jantar/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/sab_jantar.html', context)

def sab_lanches(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = SabLanches.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/sab_lanches.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/sab_lanches.html', context)

def add_lanches_sab(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = SabLanches.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = SabLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sab_lanches/'+pk, context)

    return render(request, 'dieta/sab_lanches.html')

def del_lanches_sab(request, pk):
    alimentos = Alimento.objects.all()
    obj = SabLanches.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = SabLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/sab_lanches/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/sab_lanches.html', context)

#### DOMINGO ####

def dom_desjejum(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = DomDesjejum.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/dom_desjejum.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/dom_desjejum.html', context)

def add_desjejum_dom(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = DomDesjejum.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = DomDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/dom_desjejum/'+pk, context)

    return render(request, 'dieta/dom_desjejum.html')

def del_desjejum_dom(request, pk):
    alimentos = Alimento.objects.all()
    obj = DomDesjejum.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = DomDesjejum.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/dom_desjejum/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/dom_desjejum.html', context)

def dom_almoco(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = DomAlmoco.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/dom_almoco.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/dom_almoco.html', context)

def add_almoco_dom(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = DomAlmoco.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = DomAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/dom_almoco/'+pk, context)

    return render(request, 'dieta/dom_almoco.html')

def del_almoco_dom(request, pk):
    alimentos = Alimento.objects.all()
    obj = DomAlmoco.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = DomAlmoco.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/dom_almoco/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/dom_almoco.html', context)

def dom_jantar(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = DomJantar.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/dom_jantar.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/dom_jantar.html', context)

def add_jantar_dom(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = DomJantar.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = DomJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/dom_jantar/'+pk, context)

    return render(request, 'dieta/dom_jantar.html')

def del_jantar_dom(request, pk):
    alimentos = Alimento.objects.all()
    obj = DomJantar.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = DomJantar.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/dom_jantar/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/dom_jantar.html', context)

def dom_lanches(request, pk):
    dieta = get_object_or_404 (Dieta, pk=pk)

    if request.user == dieta.user:
        alimentos = Alimento.objects.all()
        obj = DomLanches.objects.filter(dieta=dieta)

        query = request.GET.get('q')
        if query:
            alimentos = alimentos.filter(
            Q(nome__icontains=query)
            )

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return render(request, 'dieta/refeicoes/dom_lanches.html', context)

    context= {}

    return render(request, 'dieta/refeicoes/dom_lanches.html', context)

def add_lanches_dom(request, pk):
    user = request.user
    form = AlimentoForm(request.POST or None)

    if form.is_valid():
        alimento_id = form.cleaned_data.get("alimento")
        quantidade = form.cleaned_data.get("quantidade")
        dieta_id = form.cleaned_data.get("dieta")
        dieta = Dieta.objects.get(pk=dieta_id)
        alimento = Alimento.objects.get(pk=alimento_id)
        novo_desjejum, create = DomLanches.objects.get_or_create(
                        dieta = dieta,
                        alimento = alimento,
                        quantidade= quantidade,
                        )
        alimentos = Alimento.objects.all()
        obj = DomLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/dom_lanches/'+pk, context)

    return render(request, 'dieta/dom_lanches.html')

def del_lanches_dom(request, pk):
    alimentos = Alimento.objects.all()
    obj = DomLanches.objects.get(pk=pk)

    if request.method == "POST":
        dieta = Dieta.objects.get(pk=obj.dieta.pk)
        obj.delete()
        messages.success(request, 'Alimento apagado')
        obj = DomLanches.objects.filter(dieta=dieta)

        context = {
            'dieta': dieta,
            'alimentos': alimentos,
            'obj': obj
        }

        return HttpResponseRedirect('/dom_lanches/'+str(dieta.pk), context)

    context = {

    }
    return render(request, 'dieta/dom_lanches.html', context)

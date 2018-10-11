from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, HttpResponse

from publicacao.forms import PerguntaForm
from publicacao.models import Pergunta
from comentario.models import Comentario

@login_required
def submit(request):
    if request.method == "POST":
        pergunta_form = PerguntaForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if pergunta_form.is_valid():
            pergunta = pergunta_form.save(commit=False)
            pergunta.user = request.user
            pergunta.save()
            return redirect(next_url)
        else:
            return public(request, pergunta_form)
    return redirect('/')

def deletar_pergunta(request, pk):
    try:
        obj = Pergunta.objects.get(pk=pk)
    except:
        raise Http404
    if obj.user != request.user:
        response = HttpResponse('Usuário não tem permissão')
        response.status_code = 403
        return response

    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Pergunta apagada')
        return HttpResponseRedirect('/')
    context = {
        "object": obj
    }
    return render(request, "pergunta_delete.html", context)

def deletar_comentario(request, pk):
    # obj = get_object_or_404(Comentarios, pk=pk)
    try:
        obj = Comentario.objects.get(pk=pk)
    except:
        raise Http404
    if obj.user != request.user:
        # messages.success(request, 'Usuário não tem permissão')
        # raise Http404
        response = HttpResponse('Usuário não tem permissão')
        response.status_code = 403
        return response

    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Comentario apagado')
        return HttpResponseRedirect('/')
    context = {
        "object": obj
    }
    return render(request, "confirm_delete.html", context)

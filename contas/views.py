from django.shortcuts import render, redirect
from contas.formularios import (FormularioCadastro,FormularioEdicaoPerfil,)
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.views.generic import DetailView, TemplateView, ListView

def cadastro(request):
    if request.method == "POST":
        form = FormularioCadastro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FormularioCadastro()

        args = {'form' : form}
        return render(request, 'contas/cadastro.html', args)

class EntrarView(TemplateView):
    template_name = 'contas/entrar.html'

@login_required
def perfil(request):
    args = {'user': request.user}
    return render(request, 'contas/perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = FormularioEdicaoPerfil(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/perfil')

    else:
        form = FormularioEdicaoPerfil(instance=request.user)
        args = {'form': form}
        return render(request, 'contas/editar_perfil.html', args)

@login_required
def mudar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/perfil')

        else:
            return redirect('/mudar-senha')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'contas/mudar_senha.html', args)

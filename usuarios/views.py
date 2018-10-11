from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import update_session_auth_hash, login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Count
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from usuarios.tokens import account_activation_token
from usuarios.forms import AuthenticateForm, SignUpForm
from usuarios.models import PerfilEstudante
from publicacao.models import Pergunta
from comentario.models import Comentario
from comentario.forms import ComentarioForm


def entrar(request, auth_form=None, user_form=None):
    if request.user.is_authenticated:
        user = request.user

        return render(request,
                      'mairimed/inicio.html',
                      { 'user': user,
                       'next_url': '/', })
    else:
        # User is not logged in
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or SignUpForm()

        return render(request,
                      'usuarios/entrar.html',
                      {'auth_form': auth_form, 'user_form': user_form, })

@login_required
def perfil(request):
    user = request.user
    minhas_perguntas = Pergunta.objects.filter(user=user)

    users = User.objects.filter(pk=user.pk).annotate(pergunta_count=Count('pergunta'))
    perguntas = map(get_latest, users)
    obj = zip(users, perguntas)

    users_resposta = User.objects.filter(pk=user.pk).annotate(comentario_count=Count('comentario'))
    comentarios = map(get_latest, users_resposta)
    obj_comentarios = zip(users_resposta, comentarios)

    content_type = ContentType.objects.get_for_model(Pergunta)
    comentarios = Comentario.objects.filter(content_type=content_type, )

    initial_data = {
            "content_type": content_type,
    }

    comentario_form = ComentarioForm(request.POST or None, initial=initial_data)
    if comentario_form.is_valid():
            c_type = comentario_form.cleaned_data.get("content_type")
            content_type = ContentType.objects.get(model=c_type)
            object_id = request.POST.get("object_id")
            comentario_conteudo = comentario_form.cleaned_data.get("comentario")
            novo_comentario, create = Comentario.objects.get_or_create(
                                    user = request.user,
                                    content_type = content_type,
                                    object_id = object_id,
                                    conteudo = comentario_conteudo
                                    )
            return HttpResponseRedirect('/')

    context = {
        'user': user,
        'usuario_publico': usuario_publico,
        'perguntas': minhas_perguntas,
        "comentarios": comentarios,
        "comentario_form": comentario_form,
        'obj': obj,
        'obj_comentarios': obj_comentarios,
    }

    return render(request, 'usuarios/perfil.html', context)

@login_required
def usuario_publico(request, pk):
    usuario_publico = User.objects.get(pk=pk)
    usuario_perguntas = Pergunta.objects.filter(user=usuario_publico.pk)

    users = User.objects.filter(pk=usuario_publico.pk).annotate(pergunta_count=Count('pergunta'))
    perguntas = map(get_latest, users)
    obj = zip(users, perguntas)

    users_resposta = User.objects.filter(pk=usuario_publico.pk).annotate(comentario_count=Count('comentario'))
    comentarios = map(get_latest, users_resposta)
    obj_comentarios = zip(users_resposta, comentarios)

    content_type = ContentType.objects.get_for_model(Pergunta)
    comentarios = Comentario.objects.filter(content_type=content_type, )

    initial_data = {
            "content_type": content_type,
    }

    comentario_form = ComentarioForm(request.POST or None, initial=initial_data)
    if comentario_form.is_valid():
            c_type = comentario_form.cleaned_data.get("content_type")
            content_type = ContentType.objects.get(model=c_type)
            object_id = request.POST.get("object_id")
            comentario_conteudo = comentario_form.cleaned_data.get("comentario")
            novo_comentario, create = Comentario.objects.get_or_create(
                                    user = request.user,
                                    content_type = content_type,
                                    object_id = object_id,
                                    conteudo = comentario_conteudo
                                    )
            return HttpResponseRedirect('/')

    context = {
        'user': request.user,
        'usuario_publico': usuario_publico,
        'perguntas': usuario_perguntas,
        "comentarios": comentarios,
        "comentario_form": comentario_form,
        'obj': obj,
        'obj_comentarios': obj_comentarios,
    }

    return render(request, 'usuarios/usuario_publico.html', context)

def perfil_pk(request, pk):
    args = {'user': request.user}
    return render(request, 'usuarios/perfil.html')

@login_required
def follow(request):
    if request.method == "POST":
        follow_id = request.POST.get('follow', False)
        if follow_id:
            try:
                user = User.objects.get(id=follow_id)
                request.user.userprofile.follows.add(user.userprofile)
            except ObjectDoesNotExist:
                return redirect('/users/')
    return redirect('/users/')

@login_required
def unfollow(request):
    if request.method == "POST":
        follow_id = request.POST.get('unfollow', False)
        if follow_id:
            try:
                user = User.objects.get(id=follow_id)
                request.user.userprofile.follows.remove(user.userprofile)
            except ObjectDoesNotExist:
                return redirect('/users/')
    return redirect('/users/')

class EditarPerfil(UpdateView):
    model = PerfilEstudante
    fields = ['primeiro_nome', 'ultimo_nome', 'faculdade']
    template_name = 'usuarios/editar_perfil.html'
    slug_field = 'user_id'
    slug_url_kwarg = 'user_id'

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
        return render(request, 'usuarios/editar_perfil.html', args)

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
        return render(request, 'usuarios/mudar_senha.html', args)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_active = False
            user.email = form.cleaned_data.get('username')
            user.perfilestudante.email = form.cleaned_data.get('username')
            user.perfilestudante.primeiro_nome = form.cleaned_data.get('first_name')
            user.perfilestudante.ultimo_nome = form.cleaned_data.get('last_name')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('usuarios/account_activation_email.html', {
                'user': user,
                'domain': "mairimed.com",
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'usuarios/signup.html', {'form': form})

def get_latest(user):
    try:
        return user.pergunta_set.order_by('-id')[0]
    except IndexError:
        return ""

@login_required
def users(request):
    users = User.objects.all().annotate(pergunta_count=Count('pergunta'))
    perguntas = map(get_latest, users)
    obj = zip(users, perguntas)

    users_resposta = User.objects.all().annotate(comentario_count=Count('comentario'))
    comentarios = map(get_latest, users_resposta)
    obj_comentarios = zip(users_resposta, comentarios)

    return render(request,
                  'usuarios/profiles.html',
                  {'obj': obj, 'next_url': '/users/', 'obj_comentarios': obj_comentarios,
                   'user_id': request.user.perfilestudante.user_id, })

def account_activation_sent(request):
    return render(request, 'usuarios/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.perfilestudante.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'usuarios/account_activation_invalid.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('/')
        else:
            messages.error(request, 'Por favor corrija o erro indicado.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'usuarios/change_password.html', {
        'form': form
    })


def del_user(request, pk):
    try:
        u = User.objects.get(pk = pk)
        u.delete()
        messages.success(request, "The user is deleted")

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")
        return render(request, 'home.html')

    except Exception as e:
        return render(request, 'home.html',{'err':e.message})

    return render(request, 'home.html')

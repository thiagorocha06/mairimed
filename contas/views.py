from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from contas.forms import AuthenticateForm, SignUpForm

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import UpdateView

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from contas.tokens import account_activation_token

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView

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
                      'contas/entrar.html',
                      {'auth_form': auth_form, 'user_form': user_form, })

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

            user.save()
            raw_password = form.cleaned_data.get('password1')
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('contas/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def perfil_pk(request, pk):
    args = {'user': request.user}
    return render(request, 'contas/perfil.html')



def account_activation_sent(request):
    return render(request, 'contas/account_activation_sent.html')



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
    return render(request, 'contas/change_password.html', {
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

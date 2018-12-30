from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404, HttpResponseRedirect, HttpResponse
from django.db.models import Q

def novo_treino(requests):

    context = {

    }
    return render(request, 'terno/novo_treino.html', context)

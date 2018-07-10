from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from links_uteis.models import Instituicao, Link

class ViewLinkporInstituicao(ListView):
    model = Instituicao
    template_name = 'mairimed/diretrizes.html'

    def get_context_data(self, **kwargs):
        context = super(ViewLinkporInstituicao, self)\
            .get_context_data(**kwargs)

        context['links_list'] = Link.objects.all().order_by("nome")
        return context

from django.shortcuts import render, get_object_or_404, redirect
from portal_saude.models import Materia, Assunto, Patologia
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import DetailView, TemplateView, ListView
from dicionario_farmacos.models import Farmaco
from dicionario_doencas.models import Doenca
from dicionario_alimentos.models import Alimento
from dicionario_termos.models import Termo
from hitcount.views import HitCountDetailView

class MateriaMixinDetailView(object):

    model = Materia

    def get_context_data(self, **kwargs):
        context = super(MateriaMixinDetailView, self).get_context_data(**kwargs)
        context['materia_list'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
        return context

class MateriaCountHitDetailView(MateriaMixinDetailView, HitCountDetailView):
    """
    Generic hitcount class based view that will also perform the hitcount logic.
    """
    count_hit = False
    template_name = 'portal_saude/detalhe_materia.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(MateriaMixinDetailView, self).get_context_data(**kwargs)
        context['materia_list'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
        context['materia_saude'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[7]).order_by('-data_de_publicacao')[:4]
        context['materia_alimentacao'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[6]).order_by('-data_de_publicacao')[:4]
        context['materia_exercicio'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[1]).order_by('-data_de_publicacao')[:4]
        context['materia_medicamentos'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[5]).order_by('-data_de_publicacao')[:4]
        return context

class AlimentoDetailView(DetailView):

    model = Alimento
    template_name = 'portal_saude/detalhe_alimento.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(AlimentoDetailView, self).get_context_data(**kwargs)
        context['alimentos'] = Alimento.objects.order_by('-nome')
        context['alimentos_list'] = Alimento.objects.order_by('-pk')[:5]
        return context

class DoencaDetailView(DetailView):

    model = Doenca
    template_name = 'portal_saude/detalhe_doenca.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(DoencaDetailView, self).get_context_data(**kwargs)
        context['doencas'] = Doenca.objects.order_by('-nome')
        context['doencas_list'] = Doenca.objects.order_by('-pk')[:5]
        return context

class FarmacoDetailView(DetailView):

    model = Farmaco
    template_name = 'portal_saude/detalhe_farmaco.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(FarmacoDetailView, self).get_context_data(**kwargs)
        context['farmacos'] = Farmaco.objects.order_by('-nome')
        context['farmacos_list'] = Farmaco.objects.order_by('-pk')[:5]
        return context

class TermoDetailView(DetailView):

    model = Termo
    template_name = 'portal_saude/detalhe_termo.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(TermoDetailView, self).get_context_data(**kwargs)
        context['termos'] = Termo.objects.order_by('-nome')
        context['termos_list'] = Termo.objects.order_by("-pk")[:5]
        return context

class DoencasPortalView(TemplateView):
    model = Doenca
    template_name = "portal_saude/doenca_portal.html"

    def get_context_data(self, **kwargs):
        context = super(DoencasPortalView, self).get_context_data(**kwargs)
        context['doencas_list'] = Doenca.objects.order_by('-nome')
        return context

class AlimentosPortalView(TemplateView):
    model = Alimento
    template_name = "portal_saude/alimentos_portal.html"

    def get_context_data(self, **kwargs):
        context = super(AlimentosPortalView, self).get_context_data(**kwargs)
        context['alimentos_list'] = Alimento.objects.order_by('-nome')
        return context

class TermosPortalView(TemplateView):
    model = Termo
    template_name = "portal_saude/termos_portal.html"

    def get_context_data(self, **kwargs):
        context = super(TermosPortalView, self).get_context_data(**kwargs)
        context['termos_list'] = Termo.objects.order_by('-nome')
        return context

class FarmacosPortalView(TemplateView):
    model = Farmaco
    template_name = "portal_saude/farmacos_portal.html"

    def get_context_data(self, **kwargs):
        context = super(FarmacosPortalView, self).get_context_data(**kwargs)
        context['farmacos_list'] = Farmaco.objects.order_by('-nome')
        return context

class ViewMateriaPorPaotologia(ListView):
    model = Materia
    template_name = 'portal_saude/patologias_portal.html'

    def dispatch(self, request, *args, **kwargs):
        self.patologia = get_object_or_404(
            Patologia,
            patologia=self.kwargs['patologia_name']
        )

        return super(ViewMateriaPorPaotologia, self).\
            dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ViewMateriaPorPaotologia, self)\
            .get_context_data(**kwargs)

        context['patologia'] = self.patologia
        context['materia_list'] = Materia.objects.all().order_by("-data_de_publicacao")
        return context

    def get_queryset(self):
        queryset = super(ViewMateriaPorPaotologia, self).get_queryset()
        patologia_filter = list(queryset.filter(patologia=self.patologia).order_by('titulo'))
        return patologia_filter

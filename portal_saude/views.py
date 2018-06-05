from django.shortcuts import render, get_object_or_404, redirect
from portal_saude.models import Materia, Assunto, Patologia
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import DetailView, TemplateView, ListView
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
        return context

class SaudePortalView(TemplateView):
    model = Materia
    template_name = "portal_saude/saude_portal.html"

    def get_context_data(self, **kwargs):
        context = super(SaudePortalView, self).get_context_data(**kwargs)
        context['materia_saude_list'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[4]).order_by('titulo')
        return context

class AlimentacaoPortalView(TemplateView):
    model = Materia
    template_name = "portal_saude/alimentacao_portal.html"

    def get_context_data(self, **kwargs):
        context = super(AlimentacaoPortalView, self).get_context_data(**kwargs)
        context['materia_saude_list'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[3]).order_by('titulo')
        return context

class ExerciciosPortalView(TemplateView):
    model = Materia
    template_name = "portal_saude/exercicios_portal.html"

    def get_context_data(self, **kwargs):
        context = super(ExerciciosPortalView, self).get_context_data(**kwargs)
        context['materia_saude_list'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[1]).order_by('titulo')
        return context

class BemestarPortalView(TemplateView):
    model = Materia
    template_name = "portal_saude/bemestar_portal.html"

    def get_context_data(self, **kwargs):
        context = super(BemestarPortalView, self).get_context_data(**kwargs)
        context['materia_saude_list'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now(), assunto__in=[5]).order_by('titulo')
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

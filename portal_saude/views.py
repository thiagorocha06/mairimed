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
        context['materia_list'] = Materia.objects.all().order_by("-hit_count_generic__hits")
        return context

class MateriaCountHitDetailView(MateriaMixinDetailView, HitCountDetailView):
    """
    Generic hitcount class based view that will also perform the hitcount logic.
    """
    count_hit = False
    template_name = 'portal_saude/detalhe_materia.html'
    slug_field = 'url'

# class MateriaView(TemplateView):
#     model = Materia
#
#     def get_context_data(self, **kwargs):
#         context = super(MateriaMixinDetailView, self).get_context_data(**kwargs)
#         context['materia_list'] = Materia.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
#         return context

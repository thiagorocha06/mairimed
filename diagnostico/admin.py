from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _

from diagnostico.models import (
    Diagnostico, Sintoma, Recomendacao, Medicamento
)

class DiagnosticoAdminForm(forms.ModelForm):

    class Meta:
        model = Diagnostico
        exclude = []

    sintomas = forms.ModelMultipleChoiceField(
        queryset=Sintoma.objects.all(),
        required=False,
        label= ("Sintomas"),
        widget=FilteredSelectMultiple(
            verbose_name=_('Sintomas'),
            is_stacked=False))

    recomendacoes = forms.ModelMultipleChoiceField(
        queryset=Recomendacao.objects.all(),
        required=False,
        label= ("Recomendacoes"),
        widget=FilteredSelectMultiple(
            verbose_name=_('Recomendacoes'),
            is_stacked=False))

    medicamentos = forms.ModelMultipleChoiceField(
        queryset=Medicamento.objects.all(),
        required=False,
        label= ("Medicamentos"),
        widget=FilteredSelectMultiple(
            verbose_name=_('Medicamentos'),
            is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(DiagnosticoAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['sintomas'].initial =\
                self.instance.sintomas.all()

    def save(self, commit=True):
        diagnostico = super(DiagnosticoAdminForm, self).save(commit=False)
        diagnostico.save()
        diagnostico.sintomas.set(self.cleaned_data['sintomas'])
        diagnostico.recomendacoes.set(self.cleaned_data['recomendacoes'])
        diagnostico.medicamentos.set(self.cleaned_data['medicamentos'])
        self.save_m2m()
        return diagnostico

class DiagnosticoAdmin(admin.ModelAdmin):
    form = DiagnosticoAdminForm

    list_display = ['diagnostico', ]
    search_fields = ['diagnostico', ]

class SintomaAdmin(admin.ModelAdmin):
    list_display = ['sintoma', ]
    search_fields = ['sintoma', ]

class RecomendacaoAdmin(admin.ModelAdmin):
    list_display = ['recomendacao', ]
    search_fields = ['recomendacao', ]

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ['medicamento', ]
    search_fields = ['medicamento', ]

admin.site.register(Sintoma, SintomaAdmin)
admin.site.register(Diagnostico, DiagnosticoAdmin)
admin.site.register(Recomendacao, RecomendacaoAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)

from django import forms
from django.forms.widgets import RadioSelect
from dieta.models import Alimento, Dieta

class NovaDietaForm(forms.ModelForm):

    class Meta:
        model = Dieta
        fields = ['nome_dieta', 'descricao']

class DietasForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Dieta.objects.all())

class AlimentoForm(forms.Form):
    dieta = forms.CharField(required=True)
    alimento = forms.CharField(required=True)
    quantidade = forms.DecimalField(required=True)

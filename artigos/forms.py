from django import forms
from .models import Artigo

class ArtigoForm(forms.ModelForm):

    class Meta:
        model = Artigo
        fields = (
        'modulo', 'categoria',
        'titulo', 'introducao', 'classificacao', 'epidemiologia',
        'etiologia_fisiopatologia',
        'diagnostico', 'exames_complementares', 'criterios_diagnosticos', 'diagnostico_diferencial',
        'top1', 'tratamento_e_manejo',
        'profilaxia', 'prognostico', 'complicacoes', 'referencias'
        )

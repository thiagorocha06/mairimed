from django import forms
from .models import Artigo

class ArtigoForm(forms.ModelForm):

    class Meta:
        model = Artigo
        fields = (
        'modulo', 'categoria',
        'titulo', 'introducao', 'classificacao', 'epidemiologia',
        'etiologia_fisiopatologia', 'etio_top1', 'etio_texto1', 'etio_top2', 'etio_texto2', 'etio_top3', 'etio_texto3', 'etio_top4', 'etio_texto4',
        'diagnostico', 'historia_clinica', 'exame_fisico', 'exames_complementares', 'criterios_diagnosticos', 'diagnostico_diferencial',
        'top1', 'tratamento_e_manejo', 'tratamento_nao_medicamentoso', 'tratamento_medicamentoso',
        'tratamento_intervencionista',
        'profilaxia', 'prognostico', 'complicacoes', 'referencias'
        )

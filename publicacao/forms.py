from django import forms
from publicacao.models import Pergunta

class PerguntaForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'style': 'height:40px'}))

    def is_valid(self):
        form = super(PerguntaForm, self).is_valid()
        for f in self.errors.keys():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error ribbitText'})
        return form

    class Meta:
        model = Pergunta
        exclude = ('user',)

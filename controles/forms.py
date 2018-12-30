from django import forms

from controles.models import Pressao, Glicemia, Temperatura, Peso

class PressaoForm(forms.ModelForm):
    diastolica = forms.IntegerField(required=False, widget=forms.widgets.Textarea(attrs={'style': 'height:40px; width:50px'}))
    sistolica = forms.IntegerField(required=False, widget=forms.widgets.Textarea(attrs={'style': 'height:40px; width:50px'}))

    def is_valid(self):
        form = super(PressaoForm, self).is_valid()
        for f in self.errors.keys():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error ribbitText'})
        return form

    class Meta:
        model = Pressao
        fields = ['sistolica', 'diastolica', 'data', 'hora']

class GlicemiaForm(forms.ModelForm):
    glicemia = forms.IntegerField(required=False, widget=forms.widgets.Textarea(attrs={'style': 'height:40px; width:50px'}))

    def is_valid(self):
        form = super(GlicemiaForm, self).is_valid()
        for f in self.errors.keys():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error ribbitText'})
        return form

    class Meta:
        model = Glicemia
        fields = ['glicemia', 'data', 'hora']

class TemperaturaForm(forms.ModelForm):
    temperatura = forms.IntegerField(required=False, widget=forms.widgets.Textarea(attrs={'style': 'height:40px; width:50px'}))

    def is_valid(self):
        form = super(TemperaturaForm, self).is_valid()
        for f in self.errors.keys():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error ribbitText'})
        return form

    class Meta:
        model = Temperatura
        fields = ['temperatura', 'data', 'hora']

class PesoForm(forms.ModelForm):
    peso = forms.IntegerField(required=False, widget=forms.widgets.Textarea(attrs={'style': 'height:40px; width:50px'}))

    def is_valid(self):
        form = super(PesoForm, self).is_valid()
        for f in self.errors.keys():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error ribbitText'})
        return form

    class Meta:
        model = Peso
        fields = ['peso', 'data', 'hora']

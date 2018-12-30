from django import forms
from sintoma.models import Sintoma

class SintomasForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Sintoma.objects.all())

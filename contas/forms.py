from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Nome'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Sobrenome'}))
    username = forms.EmailField(widget=forms.widgets.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Confirme a senha'}))

    def is_valid(self):
        form = super(SignUpForm, self).is_valid()
        for f, error in self.errors.items():
            if f != '__all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )

class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Senha'}))

    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for f, error in self.errors.items():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

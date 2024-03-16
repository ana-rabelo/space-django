from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada', 'usuario']
        labels = {
            'descricao': 'Descrição',
            'foto': 'Fotografia',
            'data_criacao': 'Data de registro',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control input__login'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control input__login'}),
            'categoria': forms.Select(attrs={'class': 'form-control input__login'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control input__login'}),
            'foto': forms.URLInput(attrs={'class': 'form-control input__login'},),
            'data_criacao': forms.DateInput(
                format='%d-%m-%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control input__login'
                }
            ),
        }
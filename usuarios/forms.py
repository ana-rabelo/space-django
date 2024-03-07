from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Usuário', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs= {
                'class': 'form-control input__login',
                'placeholder': 'Digite seu nome de usuário'
            }
        )
    )

    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=100,
        widget=forms.PasswordInput(
            attrs= {
                'class': 'form-control input__login',
                'placeholder': 'Digite sua senha',
                'type': 'password'
            }
        )
    )

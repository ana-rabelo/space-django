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

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Usuário', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs= {
                'class': 'form-control input__login',
                'placeholder': 'Ex.: João Silva'
            }
        )
    )

    email_cadastro=forms.EmailField(
        label='E-mail', 
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs= {
                'class': 'form-control input__login',
                'placeholder': 'Ex.: joaosilva@email.com'
            }
        )
    )

    senha_cadastro=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs= {
                'class': 'form-control input__login',
                'placeholder': 'Digite sua senha',
                'type': 'password'
            }
        )
    )

    senha_cadastro_confirmacao=forms.CharField(
        label='Confirmação de Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs= {
                'class': 'form-control input__login',
                'placeholder': 'Digite sua senha novamente',
                'type': 'password'
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        if len(nome) > 2:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('O nome de usuário não pode conter espaços')
            else:
                return nome 
        else:
            raise forms.ValidationError('O nome de usuário deve ter no mínimo 2 caracteres')
        
    def clean_senha_cadastro_confirmacao(self):
        senha = self.cleaned_data.get('senha_cadastro')
        senha_confirm = self.cleaned_data.get('senha_cadastro_confirmacao')
        
        if senha and senha_confirm:
            print(senha, senha_confirm)
            if senha != senha_confirm:
                raise forms.ValidationError('As senhas não conferem')
        else:
            return senha_confirm


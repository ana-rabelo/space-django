from django.shortcuts import render

from usuarios.forms import CadastroForms, LoginForms

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    return render(request, 'usuarios/cadastro.html', {'form': form})
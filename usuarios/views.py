from django.shortcuts import redirect, render

from usuarios.forms import CadastroForms, LoginForms

from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()

            usuario = auth.authenticate(
                request,
                username=nome, 
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                return redirect('index')
            else:
                messages.warning(request, 'Usuário ou senha inválidos!')
                return render(request, 'usuarios/login.html', {'form': form})

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
      
        if form.is_valid():
            if form["senha_cadastro"].value() != form["senha_cadastro_confirmacao"].value():
                messages.warning(request, 'As senhas não coincidem!')
                return render(request, 'usuarios/cadastro.html', {'form': form})
            
            nome = form["nome_cadastro"].value()
            email = form["email_cadastro"].value()
            senha = form["senha_cadastro"].value()

            if User.objects.filter(username=nome).exists():
                messages.warning(request, 'Nome de usuário já cadastrado!')
                return render(request, 'usuarios/cadastro.html', {'form': form})
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
           
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            
            return redirect('login')
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login')
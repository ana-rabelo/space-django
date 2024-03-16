from datetime import timezone
import os
import requests
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from apps.galeria.forms import FotografiaForms
from apps.galeria.models import Fotografia

def index(request):

    if not request.user.is_authenticated:
        messages.warning(request, "Você precisa estar logado para acessar esta página.")
        return redirect('login')

    usuario = request.user

    total_imagens_salvas = Fotografia.objects.filter(usuario=usuario).count()

    save_new_images(total_imagens_salvas, usuario) 
   
    fotografias = Fotografia.objects.order_by('data_criacao').filter(usuario=usuario, publicada=True) 

    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):

    if not request.user.is_authenticated:
        messages.warning(request, "Você precisa estar logado para acessar esta página.")
        return redirect('login')
    
    item = get_object_or_404(Fotografia, pk=foto_id, usuario=request.user)
    return render(request, 'galeria/imagem.html', {"item": item})

def buscar(request):

    if not request.user.is_authenticated:
        messages.warning(request, "Você precisa estar logado para acessar esta página.")
        return redirect('login')

    fotografias = Fotografia.objects.order_by('data_criacao').filter(publicada=True) 

    if "buscar" in request.GET:
        nome = request.GET["buscar"]
        fotografias = fotografias.filter(descricao__icontains=nome)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta página.")
        return redirect('login')
    
    form = FotografiaForms
    
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            form.save()
            messages.success(request, "Imagem salva com sucesso!")
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {"form": form})

def editar_imagem(request, foto_id):

    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta página.")
        return redirect('login')

    fotografia = get_object_or_404(Fotografia, pk=foto_id, usuario=request.user)
    form = FotografiaForms(instance=fotografia)

    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, "Imagem editada com sucesso!")
            return redirect('imagem', foto_id=foto_id)

    return render(request, 'galeria/editar_imagem.html', {"form": form, "foto_id": foto_id})
    
def deletar_imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta página.")
        return redirect('login')

    fotografia = get_object_or_404(Fotografia, pk=foto_id, usuario=request.user)
    fotografia.delete()
    messages.success(request, "Imagem deletada com sucesso!")
    
    return redirect('index')

def save_new_images(total_imagens_salvas, user):
    """
    Busca novas imagens da API APOD da NASA e as salva no banco de dados.

    Args:
        total_imagens_salvas (int): O número total de imagens já salvas no banco de dados.
        user (User): O usuário que está acessando a página.

    Returns:
        None
    """

    if total_imagens_salvas < 7:
        #captura de dados da API APOD da NASA
        api_url = "https://api.nasa.gov/planetary/apod"
        API_KEY = str(os.getenv('API_KEY'))
        #count = 6 para garantir que sempre teremos 6 imagens na galeria
        params = {"api_key": API_KEY, 
                  "count": 6}
        response = requests.get(api_url, params=params)

        dados = response.json()
                
        #salva os dados no banco de dados
        for item in dados:

            #verifica se a o objeto já foi salvo e se é uma imagem
            if not Fotografia.objects.filter(nome=item["title"]).exists() and item["media_type"] == "image":
                titulo = item["title"]
                #
                legenda = f"{item.get('copyright', 'Desconhecido')} / {item['date']}"
                descricao = item["explanation"]
                foto = item['url']

                #Para determinar a categoria de cada imagem, checa se a descrição contém palavras-chave
                categorias = {"galaxy": "GALÁXIA", 
                              "star": "ESTRELA",
                              "sun": "ESTRELA", 
                              "planet": "PLANETA", 
                              "nebula": "NEBULOSA",
                              "mercury": "PLANETA",
                              "venus": "PLANETA",
                              "earth": "PLANETA",
                              "mars": "PLANETA",
                              "jupiter": "PLANETA",
                              "saturn": "PLANETA",
                              "uranus": "PLANETA",
                              "neptune": "PLANETA",
                              "pluto": "PLANETA"}
                
                #Se nenhuma palavra-chave for encontrada, a categoria é definida como "OUTRO"
                categoria = "OUTRO"

                #Checa cada palavra da descrição até encontrar uma das palavras-chave
                for word in descricao.split():
                    if word.lower() in categorias.keys():
                        categoria = categorias[word.lower()]
                        #Se uma palavra-chave for encontrada, define a categoria e a busca é encerrada
                        break

                #Salva a imagem no banco de dados
                fotografia = Fotografia(nome=titulo, 
                                    legenda=legenda, 
                                    descricao=descricao, 
                                    foto=foto, 
                                    categoria=categoria, 
                                    publicada=True, 
                                    usuario=user)
                fotografia.save()
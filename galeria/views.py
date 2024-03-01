import requests
from django.shortcuts import render

def index(request):

    api_url = "https://api.nasa.gov/planetary/apod"
    #esconder a api_key antes de fazer o commit
    api_key = "DEMO_KEY"
    params = {"api_key": api_key, 
            "count": 5}
    response = requests.get(api_url, params=params)

    dados = response.json()
        
    info_fotos = {}
    for i, foto in enumerate(dados, start=1):
        info_fotos[i] = {
            "nome": foto["title"],
            "legenda": f"{foto.get('copyright', 'Desconhecido')} / {foto["date"]}"
        }
    
    return render(request, 'galeria/index.html', {"cards": info_fotos})

def imagem(request):
    return render(request, 'galeria/imagem.html')
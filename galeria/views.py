import requests
from django.shortcuts import render

from galeria.models import Fotografia

def index(request):
    
    """ api_url = "https://api.nasa.gov/planetary/apod"

    api_key = "DEMO_KEY"
    params = {"api_key": api_key, 
                "count": 5}
    response = requests.get(api_url, params=params)

    dados = response.json()
            
    for item in dados:
        titulo = item["title"]
        legenda = f"{item.get('copyright', 'Desconhecido')} / {item["date"]}"
        descricao = item["explanation"]
        foto = item["url"]
        
        fotografia = Fotografia(nome=titulo, legenda=legenda, descricao=descricao, foto=foto)
        fotografia.save() 
    """

    fotografias = Fotografia.objects.all()    
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request):
    return render(request, 'galeria/imagem.html')
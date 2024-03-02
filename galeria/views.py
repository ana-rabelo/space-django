import requests
from django.shortcuts import get_object_or_404, render

from galeria.models import Fotografia

def index(request):
    
    total_imagens_salvas = Fotografia.objects.count()

    save_new_images(total_imagens_salvas) 
   
    fotografias = Fotografia.objects.order_by('data_criacao').filter(publicada=True) 

    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    item = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"item": item})

def save_new_images(total_imagens_salvas):
    if total_imagens_salvas < 6:
        api_url = "https://api.nasa.gov/planetary/apod"

        api_key = "DEMO_KEY"
        params = {"api_key": api_key, 
                    "count": 6}
        response = requests.get(api_url, params=params)

        dados = response.json()
                
        for item in dados:
            if not Fotografia.objects.filter(nome=item["title"]).exists():
                titulo = item["title"]
                legenda = f"{item.get('copyright', 'Desconhecido')} / {item['date']}"
                descricao = item["explanation"]
                foto = item['url']

                categorias = {"galaxy": "GALÁXIA", 
                              "star": "ESTRELA", 
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
                
                categoria = "OUTRO"

                for word in descricao.split():
                    if word.lower() in categorias.keys():
                        categoria = categorias[word.lower()]
                        break

            fotografia = Fotografia(nome=titulo, legenda=legenda, descricao=descricao, foto=foto, categoria=categoria)
            fotografia.save()
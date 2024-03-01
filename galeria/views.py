import requests
from django.shortcuts import get_object_or_404, render

from galeria.models import Fotografia

def index(request):
    
    total_imagens_salvas = Fotografia.objects.count()

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
                legenda = f"{item.get('copyright', 'Desconhecido')} / {item["date"]}"
                descricao = item["explanation"]
                foto = item["url"]
                
                fotografia = Fotografia(nome=titulo, legenda=legenda, descricao=descricao, foto=foto)
                fotografia.save() 
   
    fotografias = Fotografia.objects.all()    
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    item = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"item": item})
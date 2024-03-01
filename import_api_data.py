import requests

from galeria.models import Fotografia

api_url = "https://api.nasa.gov/planetary/apod"

api_key = "DEMO_KEY"
params = {"api_key": api_key, 
            "count": 5}
response = requests.get(api_url, params=params)

dados = response.json()
        
for item in dados:
    titulo = item["title"]
    legenda = f"{foto.get('copyright', 'Desconhecido')} / {foto["date"]}"
    descricao = item["explanation"]
    foto = item["url"]
    
    fotografia = Fotografia(nome=titulo, legenda=descricao)
    foto.save()
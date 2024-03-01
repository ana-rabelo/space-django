import requests
from django.shortcuts import render

def index(request):

    """ info_fotos = {
    1: {"nome": "Nebulosa de Carina",
        "legenda": "webbtelescope.org / NASA / James Webb"},
    2: {"nome": "Galáxia NGC 1079",
        "legenda": "nasa.org / NASA / Hubble"}   
    } """

    api_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos"
    #esconder a api_key antes de fazer o commit
    api_key = "DEMO_KEY"
    params = {'api_key': api_key}
    response = requests.get(api_url, params=params)

    data = response.json()
    photos = data.get('latest_photos', [])
        
    info_fotos = {}
    for i, photo in enumerate(photos, start=1):
        info_fotos[i] = {
            "nome": f"Foto tirada no sol {photo.get('sol')}",
            "legenda": photo.get('earth_date', 'Unknown')
        }
    
    return render(request, 'galeria/index.html', {"cards": info_fotos})

def imagem(request):
    return render(request, 'galeria/imagem.html')
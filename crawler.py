from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from urllib.parse import unquote

"""
URLS de referencia
# Para ayudar a filtrar por consola
https://archive.org/details/3DSCIA_testitem1    # 3DS
https://archive.org/details/PS2CollectionPart2ByGhostware  # PS2
https://archive.org/details/2-games-in-1-sonic-advance-sonic-battle-europe-en-ja-fr-de-es-en-ja-fr-de-es-it # GBA
"""


urls = {
    "Playstation 2":"https://archive.org/details/PS2CollectionPart2ByGhostware",
    "Game Boy Advance":"https://archive.org/details/2-games-in-1-sonic-advance-sonic-battle-europe-en-ja-fr-de-es-en-ja-fr-de-es-it",
    "Nintendo 3DS":"https://archive.org/details/3DSCIA_testitem1"}

def buscarEnlace(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    links = soup.find_all('a',string="SHOW ALL")
    
    for link in links:
        href = link.get('href')
        full_url = urljoin(url, href)
        # print(f"Enlace encontrado: {full_url}")
        return full_url


def enlaceDescarga(url, juego):
    lista = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    links = soup.find_all('a',href=True)
    if(links is None):
        return lista
    for link in links:
        href = link.get('href')
        full_url = url + '/' + href # Convertir enlaces que permitan la descarga del archivo.
        if(full_url.endswith(".7z") or full_url.endswith(".zip") or full_url.endswith(".rar") or 
            full_url.endswith(".gba")):
            descarga = unquote(full_url)
            if(juego.lower() in descarga.lower()):
                lista.append(descarga)
    return lista
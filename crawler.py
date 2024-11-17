from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from urllib.parse import unquote

"""
URLS de referencia
# Para ayudar a filtrar por consola

https://archive.org/details/3DSCIA_testitem1    # 3DS
https://archive.org/details/ps2-iso-backups-7z  # PS2
https://archive.org/details/2-games-in-1-sonic-advance-sonic-battle-europe-en-ja-fr-de-es-en-ja-fr-de-es-it # GBA

"""
url = "https://archive.org/details/ps2-iso-backups-7z"
juego = input("Titulo del Juego: ")


def entrarEnlace(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    links = soup.find_all('a',string="SHOW ALL")
    
    for link in links:
        href = link.get('href')
        full_url = urljoin(url, href)
        # print(f"Enlace encontrado: {full_url}")
        return full_url


def entrarSubenlace(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    # print(f"Titulo de la pagina: {soup.title.text}")
    links = soup.find_all('a',href=True)
    
    for link in links:
        href = link.get('href')
        full_url = url + '/' + href # Convertir enlaces que permitan la descarga del archivo.
        if(full_url.endswith(".7z") or full_url.endswith(".zip") or full_url.endswith(".rar") or 
            full_url.endswith(".gba")):
            descarga = unquote(full_url)
            if(juego.lower() in descarga.lower()):
                print (descarga)

u = entrarEnlace(url)
entrarSubenlace(u)
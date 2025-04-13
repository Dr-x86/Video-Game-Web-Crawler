from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from urllib.parse import unquote
from tkinter import messagebox

def busquedaRecursiva(lista_urls):
    lista_enlaces = [] 
    for url in lista_urls:
        enlace = buscarEnlace(url) 
        if enlace == "": 
            continue
        lista_enlaces.append(enlace)
    return lista_enlaces

def buscarEnlace(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        links = soup.find_all('a',string="SHOW ALL")
        
        for link in links:
            href = link.get('href')
            full_url = urljoin(url, href)
            return full_url
            
    except Exception as e:
        print(f" 1.- No funciona el enlace {url}, error {e}. Saltando ... ")
    
    return ""
    
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
            full_url.endswith(".gba") or full_url.endswith(".iso") or full_url.endswith(".cia") or full_url.endswith(".gz")):
            descarga = unquote(full_url)
            if(juego.lower() in descarga.lower()):
                lista.append(descarga)
    return lista
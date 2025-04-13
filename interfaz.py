import tkinter as tk
from tkinter import ttk, messagebox
from crawler import enlaceDescarga,busquedaRecursiva
import webbrowser
import threading

urls = {
    "Playstation 2":["https://archive.org/details/ps2_bob_collection","https://archive.org/details/PS2CollectionPart1ByGhostware","https://archive.org/details/PS2CollectionPart2ByGhostware"],
    "Game Boy Advance":["https://archive.org/details/2-games-in-1-sonic-advance-sonic-battle-europe-en-ja-fr-de-es-en-ja-fr-de-es-it","https://archive.org/details/unrenamed-consoles-gba"],
    "Nintendo 3DS":["https://archive.org/details/3ds-cia-eshop","https://archive.org/details/wonderswan-cias-3ds"]
}

def obtener_resultados(lista_resultado_juegos):
    bandera = True
    for resultado in lista_resultado_juegos:
        for juego in resultado:
            bandera = False
            lista_resultados.insert(tk.END, juego)
    if(bandera):
        messagebox.showinfo("No disponible","Juego no disponible aún")
        return

def buscar_juego():
    lista_resultado_juegos = []
    
    entry_juego["state"]="disable"
    btn_buscar["state"]="disable"
    
    juego = entry_juego.get().strip()
    consola = combo_consola.get().strip()

    if not juego or consola not in urls:
        messagebox.showerror("Error", "Debes ingresar el título del juego y seleccionar una consola.")
        return
    
    lista_resultados.delete(0, tk.END)
    
    lista_enlaces = busquedaRecursiva(urls[consola])
    for enlace in lista_enlaces:
        lista_resultado_juegos.append(enlaceDescarga(enlace, juego))
    
    obtener_resultados(lista_resultado_juegos)

    
    entry_juego["state"]="normal"
    btn_buscar["state"]="normal"
    
# Función para abrir el enlace seleccionado en el navegador
def abrir_enlace(event):
    seleccion = lista_resultados.curselection()
    if seleccion:
        url = lista_resultados.get(seleccion)
        webbrowser.open(url)
        
def salir():
    exit()

def inicio():
    hilo = threading.Thread(target=buscar_juego, daemon=True)
    hilo.start()

ventana = tk.Tk()
ventana.title("Bot-Crawler")
ventana.geometry("600x450")

tk.Label(ventana, text="Título del Juego:").pack(pady=5)
entry_juego = tk.Entry(ventana, width=50)
entry_juego.pack(pady=5)

tk.Label(ventana, text="Selecciona la Consola:").pack(pady=5)
combo_consola = ttk.Combobox(ventana, values=list(urls.keys()), state="readonly")
combo_consola.pack(pady=5)
combo_consola.set("Elige una consola")

btn_buscar = tk.Button(ventana, text="Buscar", command=inicio)
btn_buscar.pack(pady=10)

lista_resultados = tk.Listbox(ventana, width=70, height=10)
lista_resultados.pack(pady=10)

lista_resultados.bind("<Double-Button-1>", abrir_enlace)

boton_salir = tk.Button(ventana, text="Salir", command=salir, width=10, fg="white", bg="red")
boton_salir.pack(pady=10)

ventana.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
from crawler import urls, buscarEnlace, enlaceDescarga
import webbrowser
import threading

def buscar_juego():
    entry_juego["state"]="disable"
    btn_buscar["state"]="disable"
    
    juego = entry_juego.get().strip()
    consola = combo_consola.get().strip()
    

    if not juego or consola not in urls:
        messagebox.showerror("Error", "Debes ingresar el título del juego y seleccionar una consola.")
        return
    url_base = urls[consola]
    lista_resultados.delete(0, tk.END)

    try:
        enlace = buscarEnlace(url_base)
        resultados = enlaceDescarga(enlace, juego)
        def obtener_resultados():
            messagebox.showinfo("Buscando", "Buscando el juego en los enlaces ... ")
            for resultado in resultados:
                lista_resultados.insert(tk.END, resultado)

        obtener_resultados()
        if resultados == []:
            messagebox.showerror("Error", "No se encontró.")

    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al buscar el juego: {str(e)}")
    
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
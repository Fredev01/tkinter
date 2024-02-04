# Tkinter - Tk Interface
# importamos el modulo de tkinter
import tkinter as tk
# importamos el 
from tkinter import ttk
# Creamos un objeto usando la clase Tk
window = tk.Tk()
# Modificamos el tamanio de la ventana (pixeles)
window.geometry('1000x800')
# Cambiamos el nombre de la ventana
window.title('Hello world!!')
# Configuramos el icono de la app
# window.iconbitmap('icono.ico')
# crear el metodo
def evento_click():
    boton1.config(text="Boton presionado")
    print("Ejecucion del evento click")
    boton2 = ttk.Button(window, text="Nuevo boton")
    boton2.pack()
# Creamos un boton, el objeto padre es window
boton1 = ttk.Button(window, text='Dar click', command=evento_click)
# Utilizar el pack layout manager para mostrar el boton en la ventana
boton1.pack()
# iniciamos la ventana (esta linea la ejecutamos al final)
# Si la ejecutamos antes, no se muestran los cambios anteriores
window.mainloop()
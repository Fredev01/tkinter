import tkinter as tk
from tkinter import ttk

def evento1():
    boton1.config(text='Boton 1 presionado')
    
def evento2():
    boton2.config(text='Boton 2 presionado')
    
def evento4():
    boton4.config(text='boton 4 presionado', fg='blue', relief=tk.GROOVE, bg='yellow')
    
ventana = tk.Tk()
ventana.geometry('1200x1080')
ventana.title("Manejo de grid")
# Configurar el GRID
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)
# Definimos dos botones
boton1 = ttk.Button(ventana, text='Boton1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=20, ipady=10, columnspan=2, rowspan=2)
#   N (arriba), E (derecha), S (sur), W (izquierda)
boton2 = ttk.Button(ventana, text='Boton2', command=evento2)
# boton2.grid(row=1, column=0, sticky='NSWE')

# boton 3
boton3 = ttk.Button(ventana, text='boton3')
# boton3.grid(row=0 , column=1, sticky='NSWE')
boton4 = tk.Button(ventana, text='boton4', command=evento4)
# boton4.grid(row=1, column=1, sticky='NSWE')
ventana.mainloop() 
import tkinter as tk
from tkinter import Menu, ttk, messagebox

def enviar():
    data = input1.get()
    if data:
        messagebox.showinfo(title='Mensaje de informacion',message=data + 'Informacion')

def crear_menu():
    # Configurar el menu principal
    menu_principal = Menu(ventana)
    # tearoff = False para evitar que se separe el menu de la interfaz
    submenu_archivo = Menu(menu_principal, tearoff=False)
    # Agregamos una nueva opcion al menu de archivo
    submenu_archivo.add_command(label='Nuevo')
    # agregamos el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    # Agregamos el menu a la interfaz
    ventana.config(menu=menu_principal)
ventana = tk.Tk()
ventana.geometry('1200x1000')
ventana.title("Componente para menu")

label1 = tk.Label(ventana, text='Nombre:')
input1 = ttk.Entry(ventana, width=40)
boton_enviar = ttk.Button(ventana, text='enviar', command=enviar)
label1.grid(row=0, column=0, padx=20)
input1.grid(row=0, column=1, padx=20)
boton_enviar.grid(row=0, column=2, padx=20)

crear_menu()
ventana.mainloop()
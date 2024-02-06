import tkinter as tk
from tkinter import ttk, messagebox

def enviar():
    data = input1.get()
    if data:
        messagebox.showinfo(title='Mensaje de informacion',message=data + 'Informacion')
        messagebox.showwarning(title='Mensaje de advertencia', message= data + 'Advertencia')
        messagebox.showerror('Mensaje de ERROR', data + 'ERROR')

ventana = tk.Tk()
ventana.geometry('1200x1000')
ventana.title("Componente Messagebox")

label1 = tk.Label(ventana, text='Nombre:')
input1 = ttk.Entry(ventana, width=40)
boton_enviar = ttk.Button(ventana, text='enviar', command=enviar)
label1.grid(row=0, column=0, padx=20)
input1.grid(row=0, column=1, padx=20)
boton_enviar.grid(row=0, column=2, padx=20)

ventana.mainloop()
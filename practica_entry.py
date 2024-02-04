import tkinter as tk
from tkinter import ttk
def enviar():
    print(entrada1.get())
    boton1.config(text=entrada1.get())
    # Eliminar el contenido en la caja de texto
    # entrada1.delete(0, tk.END)
    # Seleccionar la el texto en la caja
    entrada1.select_range(0, tk.END)
    # para hacer efectiva la seleccion 
    entrada1.focus()
    
ventana = tk.Tk()
ventana.geometry('1500x1200')
ventana.title('Practicas con entry')
# ventana.rowconfigure(0, weight=2)
# width es la cantidad de caracteres
# la propiedad show sirve para ocultar el texto escrito por el user, util para password
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
# propiedad state para deshabilitar el campo 
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.DISABLED)
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)

entrada1.grid(row=0, column=0)
# insert agrega un texto
entrada1.insert(0,'Introduce una cadena')
entrada1.insert(tk.END, '.')
# entrada1.configure(state='readonly')


boton1 = ttk.Button(ventana, text='enviar', command=enviar)
boton1.grid(row=0, column=1)
ventana.mainloop()
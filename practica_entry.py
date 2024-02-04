import tkinter as tk
from tkinter import ttk
def enviar():
    # boton1.config(text=variable_ent_1.get())
    # # modificacion utilizamos la varible de texto y el metodo set
    # variable_ent_1.set('cambio....')
    # recuperar la informacion ya modificada 
    print(variable_ent_1.get())
    etiqueta1.config(text=variable_ent_1.get())
    
ventana = tk.Tk()
ventana.geometry('1500x1200')
ventana.title('Manejo de componentes')
ventana.rowconfigure(0, weight=1)
etiqueta1 = tk.Label(ventana,text='Nombre:',font='arial')
variable_ent_1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30,textvariable=variable_ent_1)

entrada1.grid(row=0, column=1, padx=20, pady=20, ipadx=20, sticky='NS')
etiqueta1.grid(row=0, column=0, padx=20, pady=20, sticky='NS')
# insert agrega un texto
# entrada1.insert(0,'Introduce una cadena')
# entrada1.insert(tk.END, '.')
# entrada1.configure(state='readonly')


boton1 = ttk.Button(ventana, text='enviar', command=enviar)
boton1.grid(row=0, column=2, padx=20, pady=15, sticky='NS')
ventana.mainloop()
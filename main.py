import tkinter as tk

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return print ("no se puede devidir entre 0")



ventana=tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x300")

etiqueta = tk.Label(ventana, text="Ingrese un numero: ")
etiqueta.pack(padx=5, pady=5)
entrada = tk.Entry(ventana)
entrada.pack()

etiqueta2= tk.Label(ventana, text="Ingrese otro numero: ")
etiqueta2.pack(padx=6, pady=6)
entrada2 = tk.Entry(ventana)
entrada2.pack()

etiqueta3= tk.Label(ventana, text="RESULTADO: ")
etiqueta3.pack(padx= 7, pady=7)
entrada3 = tk.Entry(ventana)
entrada3.pack()






ventana.mainloop()
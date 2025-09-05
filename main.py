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



def funcuines(seleccion ):
    a=float(entrada.get())
    b=float(entrada.get())

    if seleccion == "suma":
        resultado = suma(a, b)

    elif seleccion == "resta":
        resultado = resta(a, b)
    elif seleccion == "multiplicacion":
        resultado = multiplicacion(a, b)
    elif seleccion == "division":
        resultado = division(a, b)

    entrada3.delete(0, tk.END)
    entrada3.insert(0, resultado)

def botonSuma():
    a=float(entrada.get())
    b=float(entrada.get())
    resultado = suma(a, b)
    entrada3.delete(0, tk.END)
    entrada3.insert(0, resultado)

def botonResta():
    a=float(entrada.get())
    b=float(entrada.get())
    resultado = resta(a, b)
    entrada3.delete(0, tk.END)
    entrada3.insert(0, resultado)

def botonMultiplicacion():
    a=float(entrada.get())
    b=float(entrada.get())
    resultado = multiplicacion(a, b)
    entrada3.delete(0, tk.END)
    entrada3.insert(0, resultado)

def botonDivision():
    a=float(entrada.get())
    b=float(entrada.get())
    resultado = division(a, b)
    entrada3.delete(0, tk.END)
    entrada3.insert(0, resultado)






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


bSuma= tk.Button(ventana, text="SUMA", command=botonSuma)
bSuma.pack(padx=5, pady=5)

bResta= tk.Button(ventana, text="RESTA", command=botonResta)
bResta.pack(padx=5, pady=5)

bMultiplicacion=tk.Button(ventana, text="MULTIPLICACION", command=botonMultiplicacion)
bMultiplicacion.pack(padx=5, pady=5)

bdivision= tk.Button(ventana, text="DIVISION", command=botonDivision)
bdivision.pack(padx=5, pady=5)

ventana.mainloop()








ventana.mainloop()
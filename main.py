from tkinter import Tk, Button, Entry, Label

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("295x250")

# Función para obtener el valor de un botón y mostrarlo en la pantalla
def click_boton(valor):
    contenido = etiqueta.cget("text")  # Obtener el contenido actual de la etiqueta
    etiqueta.config(text=contenido + str(valor))  # Actualizar la etiqueta con el nuevo valor

# Función para evaluar la expresión matemática
def evaluar():
    try:
        resultado = eval(etiqueta.cget("text"))  # Evalúa la expresión ingresada
        etiqueta.config(text=str(resultado))  # Muestra el resultado en la etiqueta
    except:
        etiqueta.config(text="Error")  # Muestra "Error" en caso de una expresión inválida

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=10, padx=1, pady=1)

# Configuración de la etiqueta en la pantalla
etiqueta = Label(pantalla, width=40, height=2, bg="black", fg="white", borderwidth=0)
etiqueta.grid(row=0, column=0)

# Configuración botones con eventos
Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(1)).grid(row=1, column=0, padx=1, pady=1)
Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(2)).grid(row=1, column=1, padx=1, pady=1)
Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(3)).grid(row=1, column=2, padx=1, pady=1)
Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(4)).grid(row=2, column=0, padx=1, pady=1)
Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(5)).grid(row=2, column=1, padx=1, pady=1)
Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(6)).grid(row=2, column=2, padx=1, pady=1)
Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(7)).grid(row=3, column=0, padx=1, pady=1)
Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(8)).grid(row=3, column=1, padx=1, pady=1)
Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(9)).grid(row=3, column=2, padx=1, pady=1)
Button(root, text="0", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(0)).grid(row=4, column=1, padx=1, pady=1)

Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: click_boton('.')).grid(row=4, column=2, padx=1, pady=1)
Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2", command=evaluar).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: click_boton('+')).grid(row=1, column=3, padx=1, pady=1)
Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: click_boton('-')).grid(row=2, column=3, padx=1, pady=1)
Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: click_boton('*')).grid(row=3, column=3, padx=1, pady=1)
Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: click_boton('/')).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()

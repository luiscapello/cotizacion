from usuarios import acciones
from cProfile import label
from tkinter import *

#definir ventana
ventana = Tk()
ventana.geometry("650x450")
ventana.title("Uyeda Industrial de Mexico")
ventana.resizable(0,0)

ventana.config(
    bg="Teal"
)

texto = Label(ventana, text=" Bienvenido  ")
texto.config(
    fg="white",
    bg="black",
    padx=70,
    pady=20,
    font=("Arial", 25),
    cursor="trek"
)
texto.pack()

name_data = StringVar()
price_data = StringVar()

print("""
Acciones disponibles
    -Registro
    -Ingresar
""")

hazEl = acciones.Acciones()

accion = input("Que Accion deseas realizar? ")

if accion == "Registro":
    hazEl.registro()
elif accion == "Ingresar":
    hazEl.ingresar()


#definir campos de pantalla (add)
add_label = Label(ventana, text="Agregar Producto")

#crear compas del formularios
add_frame = Frame(ventana)





#cargar ventana
ventana.mainloop()
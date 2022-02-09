from tkinter import messagebox as Messagebox
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


print("""
Acciones disponibles
    -Registro
    -Ingresar
""")

hazEl = acciones.Acciones()

nombre = StringVar()
contraseña = StringVar()


usuario = Label(ventana, text="Nombre de Usuario: ")
usuario.config(
    fg="black",
    padx=10,
    pady=10,
    font=("Arial", 15),
)
usuario.grid(row=1, column=1, columnspan=12)
Entry(ventana, textvariable = nombre, justify="center").grid(row=2, column=1, columnspan=12)

contra = Label(ventana, text="Contraseña: ")
contra.config(
    fg="black",
    padx=10,
    pady=10,
    font=("Arial", 15),
)
contra.grid(row=3, column=1, columnspan=12)
Entry(ventana, textvariable = contraseña, justify="center").grid(row=4, column=1, columnspan=12)

Label(ventana, text="").pack()

Label(ventana, text="").pack(side="left")
Button(ventana, text=" Ingresar ",).pack(side="left", fill=X, expand=YES)
Label(ventana, text="").grid(row=5, column=0, columnspan=12)
Button(ventana, text=" registrarme ",).pack(side="left", fill=X, expand=YES)
Label(ventana, text="").grid(row=5, column=1, columnspan=12)
Button(ventana, text=" Olvide mi contraseña ",).pack(side="left", fill=X, expand=YES)
Label(ventana, text="").grid(row=6, column=1, columnspan=12)



accion = input("Que Accion deseas realizar? ")

if accion == "Registro":
    hazEl.registro()
elif accion == "Ingresar":
    hazEl.ingresar()


#cargar ventana
ventana.mainloop()
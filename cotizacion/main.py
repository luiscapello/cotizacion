from usuarios import acciones

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
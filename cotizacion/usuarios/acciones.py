
import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nOk!! Vamos a registrate en el sistema...")

        idEmpleado = input("Cual es tu numero de empleado:")
        nombre = input("¿Cual es tu nombre? ")
        apellidos = input("¿Cuales son tus apellidos? ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(idEmpleado, nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email} y el numero de empleado {registro[1].idEmpleado }")

        else:
            print("\nNo te has registrado correctamente !!!") 

    def ingresar(self):
        print("Vale!! identificate en el sistema")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña:")

            usuario = modelo.Usuario('','','',email, password) #pasamos los parametros que vamos a comparar
            ingresa = usuario.identificar() # guardamos los parametros

            if email == ingresa[4]:
                print(f"Bienvenido {ingresa[2]}, has ingresado correctamente")
                self.proximasAcciones(ingresa)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"login incorrecto")

    def proximasAcciones(self, usuario):
        print("""
        Acciones desponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - salir (salir)
        """)

        accion = input("\n¿Que deseas hacer?: ")
        hasEl = notas.acciones.Acciones()

        if accion == "crear":
            hasEl.crear(usuario)
            self.proximasAcciones(usuario) #retornamos la funcion hasta que el usuario salga

        elif accion == "mostrar":
            hasEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            print("\nVamos a eliminar")
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"\nhasta pronto {usuario[2]} !!")
            exit()

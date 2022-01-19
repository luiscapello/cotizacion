import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"\n Ok {usuario[2]}!! Vamos a crear una nota...")

        titulo = input("\nintroduce el titulo de tu nota: ")
        descripcion = input("\nIntroduce el contennido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")

        else:
            print(f"\nNo se ha guardado la nota {usuario[2]} ")

    def mostrar(self, usuario):
        print(f"\nVale {usuario[2]}!! Aqui tienes tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n****************************************************")
            print(nota[2])
            print(nota[3])
            print("\n****************************************************")

    def borrar(self, usuario):
        print(f"\nOK {usuario[2]}!! Vamos a borrar la nota")

        titulo = input("Introduce el titulo de la nota que quieres borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")

        else:
            print("No se a podido borra la nota, vuelvelo a intentar")
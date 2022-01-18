import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"\nOk {usuario[2]}!! Vamos a crear una nota...")

        titulo = input("introduce el titulo de tu nota: ")
        descripcion = input("Introduce el contennido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")

        else:
            print(f"\nNo se ha guardado la nota {usuario[2]} ")


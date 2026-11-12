from almacen import Almacen
from comandos.agregar import agregar
from comandos.cambiar_estado import cambiar_estado
from comandos.listar import listar


def mostrar_menu():
    print()
    print("Gestor de setlist")
    print("1. Agregar canción")
    print("2. Listar canciones")
    print("3. Cambiar estado")
    print("4. Salir")


def main():
    almacen = Almacen()
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            titulo = input("Título: ").strip()
            artista = input("Artista: ").strip()
            try:
                cancion = agregar(almacen, titulo, artista)
            except ValueError as error:
                print(error)
                continue
            print(f"Canción agregada (id {cancion.id}).")

        elif opcion == "2":
            canciones = listar(almacen)
            if not canciones:
                print("No hay canciones.")
                continue
            for cancion in canciones:
                print(
                    f"{cancion.id}. [{cancion.estado}] {cancion.titulo} — {cancion.artista}"
                )

        elif opcion == "3":
            try:
                id_cancion = int(input("Id de la canción: ").strip())
            except ValueError:
                print("El id tiene que ser un número.")
                continue
            estado = input("Estado (pendiente, ensayada, tocada): ").strip()
            try:
                cancion = cambiar_estado(almacen, id_cancion, estado)
            except ValueError as error:
                print(error)
                continue
            if cancion is None:
                print("No existe una canción con ese id.")
            else:
                print(f"Canción {cancion.id} ahora está {cancion.estado}.")

        elif opcion == "4":
            print("Hasta luego.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

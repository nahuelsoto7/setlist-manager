from tareas import agregar, completar, listar


def mostrar_menu():
    print()
    print("Lista de tareas")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar como completada")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            texto = input("Texto de la tarea: ").strip()
            if not texto:
                print("La tarea no puede estar vacía.")
                continue
            tarea = agregar(texto)
            print(f"Tarea agregada (id {tarea['id']}).")

        elif opcion == "2":
            tareas = listar()
            if not tareas:
                print("No hay tareas.")
                continue
            for tarea in tareas:
                estado = "completada" if tarea["completada"] else "pendiente"
                print(f"{tarea['id']}. [{estado}] {tarea['texto']}")

        elif opcion == "3":
            try:
                id_tarea = int(input("Id de la tarea: ").strip())
            except ValueError:
                print("El id tiene que ser un número.")
                continue
            tarea = completar(id_tarea)
            if tarea is None:
                print("No existe una tarea con ese id.")
            else:
                print(f"Tarea {tarea['id']} marcada como completada.")

        elif opcion == "4":
            print("Hasta luego.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

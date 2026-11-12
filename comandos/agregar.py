from modelo import Cancion


def agregar(almacen, titulo, artista):
    titulo = titulo.strip()
    artista = artista.strip()
    if not titulo:
        raise ValueError("El título no puede estar vacío.")
    if not artista:
        raise ValueError("El artista no puede estar vacío.")

    canciones = almacen.cargar()
    nuevo_id = max((cancion.id for cancion in canciones), default=0) + 1
    cancion = Cancion(
        id=nuevo_id,
        titulo=titulo,
        artista=artista,
        estado="pendiente",
    )
    canciones.append(cancion)
    almacen.guardar(canciones)
    return cancion

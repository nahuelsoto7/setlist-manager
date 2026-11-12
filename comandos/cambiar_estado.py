from modelo import ESTADOS


def cambiar_estado(almacen, id_cancion, estado):
    if estado not in ESTADOS:
        raise ValueError("Estado no válido. Usá pendiente, ensayada o tocada.")

    canciones = almacen.cargar()
    for cancion in canciones:
        if cancion.id == id_cancion:
            cancion.estado = estado
            almacen.guardar(canciones)
            return cancion
    return None

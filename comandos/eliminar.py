def eliminar_cancion(canciones, id_a_eliminar):
    """Elimina una canción por su ID. Devuelve la canción eliminada o None si no existe."""
    for i, cancion in enumerate(canciones):
        if cancion['id'] == id_a_eliminar:
            return canciones.pop(i)
    return None
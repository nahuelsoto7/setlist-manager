def buscar_canciones(canciones, texto_busqueda):
    """Busca canciones por título o artista (ignorando mayúsculas/minúsculas)."""
    texto_lower = texto_busqueda.lower()
    resultados = []
    for cancion in canciones:
        if texto_lower in cancion['titulo'].lower() or texto_lower in cancion['artista'].lower():
            resultados.append(cancion)
    return resultados
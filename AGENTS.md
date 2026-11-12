# Reglas de oro

1. Separación de responsabilidades. `main.py` solo muestra el menú y delega. `modelo.py` define la canción. `almacen.py` solo lee y escribe JSON. Cada archivo de `comandos/` hace una sola operación.
2. Verificación con `unittest`. Las pruebas viven en `tests/` y se corren con `py -3 -m unittest`.
3. Estructura fija:
   - `main.py`: menú.
   - `modelo.py`: datos de la canción (`id`, `titulo`, `artista`, `estado`).
   - `almacen.py`: persistencia. La ruta del archivo se inyecta para que los tests usen un archivo temporal.
   - `comandos/agregar.py`, `comandos/listar.py`, `comandos/cambiar_estado.py`: operaciones independientes.
   - `setlist.json`: datos de la aplicación.
   - `tests/`: pruebas que no tocan el `setlist.json` real.
4. No incluir `__pycache__/` ni archivos temporales en los commits.

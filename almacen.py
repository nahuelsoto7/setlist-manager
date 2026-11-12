import json
from pathlib import Path

from modelo import Cancion

RUTA_POR_DEFECTO = Path(__file__).parent / "setlist.json"


class Almacen:
    def __init__(self, ruta=None):
        self.ruta = Path(ruta) if ruta is not None else RUTA_POR_DEFECTO

    def cargar(self):
        if not self.ruta.exists():
            return []
        with self.ruta.open(encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Cancion.desde_dict(item) for item in datos]

    def guardar(self, canciones):
        datos = [cancion.a_dict() for cancion in canciones]
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        with self.ruta.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
            archivo.write("\n")

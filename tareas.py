import json
from pathlib import Path

ARCHIVO = Path(__file__).parent / "tareas.json"


def cargar():
    if not ARCHIVO.exists():
        return []
    with ARCHIVO.open(encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar(tareas):
    with ARCHIVO.open("w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, ensure_ascii=False, indent=2)


def agregar(texto):
    tareas = cargar()
    nuevo_id = max((tarea["id"] for tarea in tareas), default=0) + 1
    tarea = {"id": nuevo_id, "texto": texto, "completada": False}
    tareas.append(tarea)
    guardar(tareas)
    return tarea


def listar():
    return cargar()


def completar(id_tarea):
    tareas = cargar()
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
            guardar(tareas)
            return tarea
    return None

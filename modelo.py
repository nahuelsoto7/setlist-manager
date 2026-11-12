from dataclasses import asdict, dataclass

ESTADOS = ("pendiente", "ensayada", "tocada")


@dataclass
class Cancion:
    id: int
    titulo: str
    artista: str
    estado: str

    def a_dict(self):
        return asdict(self)

    @classmethod
    def desde_dict(cls, datos):
        return cls(
            id=int(datos["id"]),
            titulo=datos["titulo"],
            artista=datos["artista"],
            estado=datos["estado"],
        )

import tempfile
import unittest
from pathlib import Path

from almacen import Almacen
from comandos.agregar import agregar


class TestAgregar(unittest.TestCase):
    def setUp(self):
        self.setlist_real = Path("setlist.json")
        self.antes = (
            self.setlist_real.read_text(encoding="utf-8")
            if self.setlist_real.exists()
            else None
        )
        self.temporal = tempfile.TemporaryDirectory()
        self.ruta = Path(self.temporal.name) / "setlist.json"
        self.almacen = Almacen(self.ruta)

    def tearDown(self):
        self.temporal.cleanup()
        if self.antes is None:
            self.assertFalse(self.setlist_real.exists())
        else:
            self.assertEqual(
                self.setlist_real.read_text(encoding="utf-8"),
                self.antes,
            )

    def test_agrega_cancion_en_archivo_temporal(self):
        cancion = agregar(self.almacen, "Tema nuevo", "Banda local")

        self.assertEqual(cancion.id, 1)
        self.assertEqual(cancion.titulo, "Tema nuevo")
        self.assertEqual(cancion.artista, "Banda local")
        self.assertEqual(cancion.estado, "pendiente")
        guardadas = self.almacen.cargar()
        self.assertEqual(len(guardadas), 1)
        self.assertEqual(guardadas[0].titulo, "Tema nuevo")

    def test_rechaza_titulo_vacio(self):
        with self.assertRaises(ValueError):
            agregar(self.almacen, "   ", "Banda local")
        self.assertEqual(self.almacen.cargar(), [])

    def test_rechaza_artista_vacio(self):
        with self.assertRaises(ValueError):
            agregar(self.almacen, "Tema nuevo", "  ")
        self.assertEqual(self.almacen.cargar(), [])


if __name__ == "__main__":
    unittest.main()

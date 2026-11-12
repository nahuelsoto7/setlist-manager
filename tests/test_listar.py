import tempfile
import unittest
from pathlib import Path

from almacen import Almacen
from comandos.agregar import agregar
from comandos.listar import listar


class TestListar(unittest.TestCase):
    def setUp(self):
        self.setlist_real = Path("setlist.json")
        self.antes = (
            self.setlist_real.read_text(encoding="utf-8")
            if self.setlist_real.exists()
            else None
        )
        self.temporal = tempfile.TemporaryDirectory()
        self.almacen = Almacen(Path(self.temporal.name) / "setlist.json")

    def tearDown(self):
        self.temporal.cleanup()
        if self.antes is None:
            self.assertFalse(self.setlist_real.exists())
        else:
            self.assertEqual(
                self.setlist_real.read_text(encoding="utf-8"),
                self.antes,
            )

    def test_lista_vacia(self):
        self.assertEqual(listar(self.almacen), [])

    def test_lista_las_canciones_guardadas(self):
        agregar(self.almacen, "Primera", "Ana")
        agregar(self.almacen, "Segunda", "Luis")

        canciones = listar(self.almacen)

        self.assertEqual([cancion.titulo for cancion in canciones], ["Primera", "Segunda"])
        self.assertEqual([cancion.id for cancion in canciones], [1, 2])


if __name__ == "__main__":
    unittest.main()

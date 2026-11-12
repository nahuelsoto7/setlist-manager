import tempfile
import unittest
from pathlib import Path

from almacen import Almacen
from comandos.agregar import agregar
from comandos.cambiar_estado import cambiar_estado


class TestCambiarEstado(unittest.TestCase):
    def setUp(self):
        self.setlist_real = Path("setlist.json")
        self.antes = (
            self.setlist_real.read_text(encoding="utf-8")
            if self.setlist_real.exists()
            else None
        )
        self.temporal = tempfile.TemporaryDirectory()
        self.almacen = Almacen(Path(self.temporal.name) / "setlist.json")
        self.cancion = agregar(self.almacen, "Tema", "Banda")

    def tearDown(self):
        self.temporal.cleanup()
        if self.antes is None:
            self.assertFalse(self.setlist_real.exists())
        else:
            self.assertEqual(
                self.setlist_real.read_text(encoding="utf-8"),
                self.antes,
            )

    def test_cambia_a_ensayada(self):
        actualizada = cambiar_estado(self.almacen, self.cancion.id, "ensayada")

        self.assertEqual(actualizada.estado, "ensayada")
        self.assertEqual(self.almacen.cargar()[0].estado, "ensayada")

    def test_id_inexistente_no_modifica_el_archivo(self):
        antes = self.almacen.ruta.read_text(encoding="utf-8")

        resultado = cambiar_estado(self.almacen, 99, "tocada")

        self.assertIsNone(resultado)
        self.assertEqual(self.almacen.ruta.read_text(encoding="utf-8"), antes)

    def test_estado_invalido_no_guarda(self):
        antes = self.almacen.ruta.read_text(encoding="utf-8")

        with self.assertRaises(ValueError):
            cambiar_estado(self.almacen, self.cancion.id, "inventado")

        self.assertEqual(self.almacen.ruta.read_text(encoding="utf-8"), antes)


if __name__ == "__main__":
    unittest.main()

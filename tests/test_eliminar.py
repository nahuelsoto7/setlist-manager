import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from comandos.eliminar import eliminar_cancion

class TestEliminar(unittest.TestCase):
    def setUp(self):
        self.canciones = [
            {'id': 1, 'titulo': 'Bohemian Rhapsody', 'artista': 'Queen', 'estado': 'tocada'},
            {'id': 2, 'titulo': 'Imagine', 'artista': 'John Lennon', 'estado': 'ensayada'},
            {'id': 3, 'titulo': 'Hotel California', 'artista': 'Eagles', 'estado': 'pendiente'},
        ]
    
    def test_eliminar_cancion_existente(self):
        eliminada = eliminar_cancion(self.canciones, 2)
        self.assertIsNotNone(eliminada)
        self.assertEqual(eliminada['titulo'], 'Imagine')
        self.assertEqual(len(self.canciones), 2)
    
    def test_eliminar_cancion_inexistente(self):
        eliminada = eliminar_cancion(self.canciones, 99)
        self.assertIsNone(eliminada)
        self.assertEqual(len(self.canciones), 3)

if __name__ == '__main__':
    unittest.main()
import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from comandos.buscar import buscar_canciones

class TestBuscar(unittest.TestCase):
    def setUp(self):
        self.canciones = [
            {'id': 1, 'titulo': 'Bohemian Rhapsody', 'artista': 'Queen', 'estado': 'tocada'},
            {'id': 2, 'titulo': 'Imagine', 'artista': 'John Lennon', 'estado': 'ensayada'},
            {'id': 3, 'titulo': 'Hotel California', 'artista': 'Eagles', 'estado': 'pendiente'},
        ]
    
    def test_buscar_por_titulo(self):
        resultados = buscar_canciones(self.canciones, 'bohemian')
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]['titulo'], 'Bohemian Rhapsody')
    
    def test_buscar_por_artista(self):
        resultados = buscar_canciones(self.canciones, 'queen')
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]['artista'], 'Queen')
    
    def test_buscar_sin_resultados(self):
        resultados = buscar_canciones(self.canciones, 'xyz')
        self.assertEqual(len(resultados), 0)

if __name__ == '__main__':
    unittest.main()
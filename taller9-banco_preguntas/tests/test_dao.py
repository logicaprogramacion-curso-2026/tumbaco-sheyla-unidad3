import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.dao import PreguntaDAO
from src.entidad import Pregunta

def test_conexion():
    dao = PreguntaDAO(":memory:")
    assert dao is not None
    print("test_conexion: OK")

def test_insertar_y_obtener():
    dao = PreguntaDAO(":memory:")
    p = Pregunta(1, "Que es Python?", "Lenguaje", "Compilador", "Sistema", "Navegador", "A", "Facil", "Conceptos")
    dao.insertar(p)
    obtenida = dao.obtener_por_id(1)
    assert obtenida.id == 1
    print("test_insertar_y_obtener: OK")

if __name__ == "__main__":
    test_conexion()
    test_insertar_y_obtener()
    print("TODAS LAS PRUEBAS PASARON")
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.entidad import Pregunta

def test_crear_pregunta():
    p = Pregunta(1, "Que es Python?", "Lenguaje", "Compilador", "Sistema", "Navegador", "A", "Facil", "Conceptos")
    assert p.id == 1
    assert p.pregunta == "Que es Python?"
    print("test_crear_pregunta: OK")

def test_to_dict():
    p = Pregunta(1, "Que es Python?", "Lenguaje", "Compilador", "Sistema", "Navegador", "A", "Facil", "Conceptos")
    d = p.to_dict()
    assert d['id'] == 1
    assert d['tema'] == "Conceptos"
    print("test_to_dict: OK")

if __name__ == "__main__":
    test_crear_pregunta()
    test_to_dict()
    print("TODAS LAS PRUEBAS PASARON")
import unittest
from models.actividad import Actividad
from models.usuario import Usuario
from services.evaluador import EvaluadorActividades

class TestEvaluador(unittest.TestCase):
    def setUp(self):
        self.usuario = Usuario("Usuario Test")
        self.actividad = Actividad("Test", "taller", "intermedio")
        self.evaluador = EvaluadorActividades()
    
    def test_procesamiento_completo(self):
        resultado = self.evaluador.procesar_evaluacion(
            self.usuario, 
            self.actividad, 
            75
        )
        
        self.assertIsNotNone(resultado['evaluacion'])
        self.assertIsNotNone(resultado['analisis'])
        self.assertIsNotNone(resultado['informe'])
        self.assertEqual(resultado['analisis']['nivel_usuario'], 'intermedio')
    
    def test_nivel_basico(self):
        resultado = self.evaluador.procesar_evaluacion(
            self.usuario, 
            self.actividad, 
            50
        )
        self.assertEqual(resultado['analisis']['nivel_usuario'], 'basico')
    
    def test_nivel_avanzado(self):
        resultado = self.evaluador.procesar_evaluacion(
            self.usuario, 
            self.actividad, 
            90
        )
        self.assertEqual(resultado['analisis']['nivel_usuario'], 'avanzado')

if __name__ == '__main__':
    unittest.main()
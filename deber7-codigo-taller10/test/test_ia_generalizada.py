import unittest
from models.actividad import Actividad
from models.usuario import Usuario
from models.evaluacion import Evaluacion
from services.ia_generalizada import IAGeneralizada

class TestIAGeneralizada(unittest.TestCase):
    def setUp(self):
        self.ia = IAGeneralizada()
        self.usuario = Usuario("Usuario Test")
        self.actividad = Actividad("Test Actividad", "taller", "intermedio")
    
    def test_analisis_completo(self):
        evaluacion = Evaluacion(self.usuario, self.actividad, 75)
        evaluacion.evaluar_nivel(75)
        evaluacion.generar_resultado()
        
        analisis = self.ia.analizar(evaluacion)
        
        self.assertIsNotNone(analisis)
        self.assertEqual(analisis['usuario'], "Usuario Test")
        self.assertIn('brecha_habilidades', analisis)
        self.assertIn('recomendacion', analisis)
        self.assertIn('confianza_analisis', analisis)
    
    def test_calculo_brecha(self):
        brecha = self.ia._calcular_brecha('basico', 'intermedio')
        self.assertIn("Faltan", brecha)
        
        brecha_igual = self.ia._calcular_brecha('intermedio', 'intermedio')
        self.assertIn("alineado", brecha_igual)
    
    def test_recomendaciones(self):
        recomendacion = self.ia._generar_recomendacion('basico', 'taller', True)
        self.assertIn("introductorios", recomendacion)
        
        recomendacion = self.ia._generar_recomendacion('avanzado', 'cluber', True)
        self.assertIn("mentor", recomendacion)
    
    def test_patrones(self):
        evaluacion = Evaluacion(self.usuario, self.actividad, 90)
        evaluacion.nivel_usuario = 'avanzado'
        evaluacion.actividad.nivel_requerido = 'intermedio'
        
        patrones = self.ia._analizar_patrones(evaluacion)
        self.assertTrue(any("sobrecalificado" in p for p in patrones))

if __name__ == '__main__':
    unittest.main()
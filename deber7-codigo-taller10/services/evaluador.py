from models.evaluacion import Evaluacion
from services.ia_generalizada import IAGeneralizada
from services.generador_informe import GeneradorInforme
from database import db
import logging

logger = logging.getLogger(__name__)

class EvaluadorActividades:
    def __init__(self):
        self.ia = IAGeneralizada()
        self.generador_informe = GeneradorInforme()
        self.db = db
        logger.info("Evaluador de actividades inicializado")
    
    def procesar_evaluacion(self, usuario, actividad, puntaje):
        try:
            print(f"Seleccionado: {usuario.nombre} - Actividad: {actividad.nombre}")
            
            # 1. Crear evaluación
            evaluacion = Evaluacion(usuario, actividad, puntaje)
            nivel = evaluacion.evaluar_nivel(puntaje)
            print(f"Nivel evaluado: {nivel}")
            
            # 2. Generar resultado
            resultado = evaluacion.generar_resultado()
            
            # 3. IA Generalizada analiza
            print("🔄 IA Generalizada analizando el caso...")
            analisis = self.ia.analizar(evaluacion)
            print("✅ Análisis de IA completado")
            
            # 4. Guardar en base de datos
            self._guardar_evaluacion(evaluacion, analisis)
            
            # 5. Generar informe
            informe = self.generador_informe.generar(evaluacion, analisis)
            
            return {
                'evaluacion': evaluacion,
                'analisis': analisis,
                'informe': informe
            }
            
        except Exception as e:
            logger.error(f"Error procesando evaluación: {str(e)}")
            raise
    
    def _guardar_evaluacion(self, evaluacion, analisis):
        """Guarda la evaluación en la base de datos"""
        try:
            # Guardar usuario
            usuario_id = self._guardar_usuario(evaluacion.usuario)
            
            # Guardar actividad
            actividad_id = self._guardar_actividad(evaluacion.actividad)
            
            # Guardar evaluación
            query = '''
                INSERT INTO evaluaciones 
                (usuario_id, actividad_id, puntaje, nivel_usuario, resultado, 
                 recomendacion, confianza_ia)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            params = (
                usuario_id,
                actividad_id,
                evaluacion.puntaje,
                evaluacion.nivel_usuario,
                evaluacion.resultado,
                evaluacion.recomendacion,
                analisis['confianza_analisis']
            )
            cursor = self.db.ejecutar_consulta(query, params)
            evaluacion_id = cursor.lastrowid
            
            # Guardar análisis IA
            query_ia = '''
                INSERT INTO analisis_ia 
                (evaluacion_id, brecha_habilidades, patrones_detectados, detalle_analisis)
                VALUES (?, ?, ?, ?)
            '''
            params_ia = (
                evaluacion_id,
                analisis['brecha_habilidades'],
                ', '.join(analisis['patrones_detectados']),
                analisis['recomendacion']
            )
            self.db.ejecutar_consulta(query_ia, params_ia)
            
            logger.info(f"Evaluación guardada con ID: {evaluacion_id}")
            
        except Exception as e:
            logger.error(f"Error guardando evaluación: {str(e)}")
            raise
    
    def _guardar_usuario(self, usuario):
        """Guarda o actualiza un usuario"""
        query = "INSERT OR IGNORE INTO usuarios (nombre, nivel) VALUES (?, ?)"
        params = (usuario.nombre, usuario.nivel)
        self.db.ejecutar_consulta(query, params)
        
        # Obtener ID
        query_id = "SELECT id FROM usuarios WHERE nombre = ?"
        result = self.db.obtener_datos(query_id, (usuario.nombre,))
        return result[0][0] if result else None
    
    def _guardar_actividad(self, actividad):
        """Guarda o actualiza una actividad"""
        query = '''
            INSERT OR IGNORE INTO actividades 
            (nombre, tipo, nivel_requerido, acepta_consejos) 
            VALUES (?, ?, ?, ?)
        '''
        params = (
            actividad.nombre,
            actividad.tipo,
            actividad.nivel_requerido,
            1 if actividad.acepta_consejos else 0
        )
        self.db.ejecutar_consulta(query, params)
        
        # Obtener ID
        query_id = "SELECT id FROM actividades WHERE nombre = ? AND tipo = ?"
        result = self.db.obtener_datos(query_id, (actividad.nombre, actividad.tipo))
        return result[0][0] if result else None
    
    def obtener_estadisticas_ia(self):
        """Obtiene estadísticas de la IA"""
        return self.ia.obtener_estadisticas()
    
    def obtener_historial_usuario(self, usuario):
        """Obtiene el historial de evaluaciones de un usuario"""
        query = '''
            SELECT e.*, a.nombre as actividad_nombre 
            FROM evaluaciones e
            JOIN actividades a ON e.actividad_id = a.id
            JOIN usuarios u ON e.usuario_id = u.id
            WHERE u.nombre = ?
            ORDER BY e.fecha DESC
        '''
        return self.db.obtener_datos(query, (usuario.nombre,))
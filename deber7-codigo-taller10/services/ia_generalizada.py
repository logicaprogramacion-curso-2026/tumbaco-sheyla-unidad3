from datetime import datetime
import json
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class IAGeneralizada:
    """
    IA Generalizada que analiza los resultados de evaluación
    y genera recomendaciones inteligentes
    """
    
    def __init__(self):
        self.historial_analisis = []
        self.modelo_decision = {
            'basico': {
                'taller': 'recomendado para aprendizaje inicial',
                'cluber': 'requiere nivel intermedio mínimo'
            },
            'intermedio': {
                'taller': 'nivel adecuado para profundizar',
                'cluber': 'buen nivel para participar'
            },
            'avanzado': {
                'taller': 'sobrecalificado, recomendar como mentor',
                'cluber': 'nivel experto, recomendar liderazgo'
            }
        }
        logger.info("IA Generalizada inicializada")
    
    def analizar(self, evaluacion):
        """
        IA Generalizada analiza el caso completo
        """
        try:
            logger.info(f"Analizando evaluación para usuario: {evaluacion.usuario}")
            
            # Análisis profundo del caso
            nivel_usuario = evaluacion.nivel_usuario
            tipo_actividad = evaluacion.actividad.tipo
            nivel_requerido = evaluacion.actividad.nivel_requerido
            
            # Análisis de brecha de habilidades
            brecha = self._calcular_brecha(nivel_usuario, nivel_requerido)
            
            # Generar recomendación personalizada
            recomendacion = self._generar_recomendacion(
                nivel_usuario, 
                tipo_actividad,
                evaluacion.actividad.acepta_consejos
            )
            
            # Análisis de patrones
            patrones = self._analizar_patrones(evaluacion)
            
            # Calcular confianza
            confianza = self._calcular_confianza(evaluacion)
            evaluacion.confianza_ia = confianza
            
            # Crear análisis completo
            analisis = {
                'usuario': evaluacion.usuario.nombre if hasattr(evaluacion.usuario, 'nombre') else evaluacion.usuario,
                'actividad': evaluacion.actividad.nombre,
                'tipo_actividad': tipo_actividad,
                'nivel_usuario': nivel_usuario,
                'nivel_requerido': nivel_requerido,
                'brecha_habilidades': brecha,
                'recomendacion': recomendacion,
                'patrones_detectados': patrones,
                'resultado': evaluacion.resultado,
                'timestamp': datetime.now().isoformat(),
                'confianza_analisis': confianza
            }
            
            self.historial_analisis.append(analisis)
            logger.info(f"Análisis completado con confianza: {confianza:.2%}")
            return analisis
            
        except Exception as e:
            logger.error(f"Error en análisis de IA: {str(e)}")
            raise
    
    def _calcular_brecha(self, nivel_usuario, nivel_requerido):
        """Calcula la brecha entre el nivel del usuario y el requerido"""
        niveles = {'basico': 1, 'intermedio': 2, 'avanzado': 3}
        brecha = niveles.get(nivel_requerido, 0) - niveles.get(nivel_usuario, 0)
        
        if brecha > 0:
            return f"Faltan {brecha} nivel(es) para alcanzar el requerido"
        elif brecha < 0:
            return f"Supera por {abs(brecha)} nivel(es) el requerido"
        else:
            return "Nivel perfectamente alineado"
    
    def _generar_recomendacion(self, nivel, tipo, acepta_consejos):
        """Genera recomendaciones personalizadas según el perfil"""
        if not acepta_consejos:
            return "El usuario no acepta consejos - Recomendación automática no aplicable"
        
        base_recomendacion = self.modelo_decision.get(nivel, {}).get(tipo, "")
        
        # Personalizar según el nivel
        if nivel == 'basico':
            recomendacion = f"Recomendación: {base_recomendacion}. Sugerir cursos introductorios"
        elif nivel == 'intermedio':
            recomendacion = f"Recomendación: {base_recomendacion}. Practicar con proyectos reales"
        else: # avanzado
            recomendacion = f"Recomendación: {base_recomendacion}. Considerar rol de mentor"
        
        return recomendacion
    
    def _analizar_patrones(self, evaluacion):
        """Analiza patrones en el comportamiento del usuario"""
        patrones = []
        
        # Patrón de sobre-calificación
        brecha = self._calcular_brecha(
            evaluacion.nivel_usuario, 
            evaluacion.actividad.nivel_requerido
        )
        if "Supera" in brecha:
            patrones.append("Usuario sobrecalificado para la actividad")
        
        # Patrón de necesidad de mejora
        if (evaluacion.nivel_usuario == 'basico' and 
            evaluacion.actividad.nivel_requerido == 'avanzado'):
            patrones.append("Gran brecha de habilidades - Requiere preparación extensiva")
        
        # Patrón de consistencia
        if evaluacion.nivel_usuario == evaluacion.actividad.nivel_requerido:
            patrones.append("Nivel perfectamente alineado - Usuario ideal para la actividad")
        
        return patrones
    
    def _calcular_confianza(self, evaluacion):
        """Calcula el nivel de confianza del análisis"""
        confianza_base = 0.85
        
        # Factores que aumentan la confianza
        if evaluacion.actividad.acepta_consejos:
            confianza_base += 0.05
        
        if evaluacion.nivel_usuario in ['basico', 'intermedio', 'avanzado']:
            confianza_base += 0.05
        
        # Factor de puntaje
        if evaluacion.puntaje and 40 <= evaluacion.puntaje <= 100:
            confianza_base += 0.05
        
        return min(confianza_base, 0.98)
    
    def obtener_estadisticas(self):
        """Retorna estadísticas de todos los análisis realizados"""
        if not self.historial_analisis:
            return {"mensaje": "No hay análisis realizados aún"}
        
        total = len(self.historial_analisis)
        aprobados = sum(1 for h in self.historial_analisis 
                       if h['resultado'] == 'aprobado')
        
        # Análisis de niveles
        niveles = {}
        for h in self.historial_analisis:
            nivel = h['nivel_usuario']
            niveles[nivel] = niveles.get(nivel, 0) + 1
        
        # Promedio de confianza
        confianza_promedio = sum(h['confianza_analisis'] 
                               for h in self.historial_analisis) / total
        
        return {
            'total_analisis': total,
            'aprobados': aprobados,
            'tasa_exito': f"{(aprobados/total)*100:.1f}%" if total > 0 else "0%",
            'distribucion_niveles': niveles,
            'confianza_promedio': f"{confianza_promedio:.2%}",
            'total_patrones': sum(len(h['patrones_detectados']) 
                                 for h in self.historial_analisis)
        }
    
    def generar_analisis_detallado(self, evaluacion):
        """Genera un análisis detallado en formato texto"""
        analisis = self.analizar(evaluacion)
        
        informe_texto = f"""
=== ANÁLISIS DE IA GENERALIZADA ===
Fecha y Hora: {analisis['timestamp']}

DATOS DEL USUARIO:
- Usuario: {analisis['usuario']}
- Nivel Actual: {analisis['nivel_usuario']}

DATOS DE LA ACTIVIDAD:
- Actividad: {analisis['actividad']}
- Tipo: {analisis['tipo_actividad']}
- Nivel Requerido: {analisis['nivel_requerido']}

ANÁLISIS:
- Brecha de Habilidades: {analisis['brecha_habilidades']}
- Resultado: {analisis['resultado']}
- Confianza del Análisis: {analisis['confianza_analisis']:.2%}

RECOMENDACIÓN:
{analisis['recomendacion']}

PATRONES DETECTADOS:
{chr(10).join(f'- {p}' for p in analisis['patrones_detectados']) if analisis['patrones_detectados'] else 'No se detectaron patrones específicos'}
"""
        return informe_texto
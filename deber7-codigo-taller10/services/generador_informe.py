from datetime import datetime
import os
import logging
from config.settings import RUTAS

logger = logging.getLogger(__name__)

class GeneradorInforme:
    def __init__(self):
        self.informes = []
        self.carpeta_informes = RUTAS['INFORMES']
        os.makedirs(self.carpeta_informes, exist_ok=True)
        logger.info("Generador de informes inicializado")
    
    def generar(self, evaluacion, analisis):
        informe = {
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'usuario': evaluacion.usuario.nombre if hasattr(evaluacion.usuario, 'nombre') else evaluacion.usuario,
            'actividad': evaluacion.actividad.nombre,
            'tipo_actividad': evaluacion.actividad.tipo,
            'nivel_usuario': evaluacion.nivel_usuario,
            'nivel_requerido': evaluacion.actividad.nivel_requerido,
            'resultado': evaluacion.resultado,
            'recomendacion': evaluacion.recomendacion,
            'acepta_consejos': evaluacion.actividad.acepta_consejos,
            'analisis_ia': analisis,
            'brecha_habilidades': analisis.get('brecha_habilidades', ''),
            'confianza_ia': analisis.get('confianza_analisis', 0),
            'patrones_detectados': analisis.get('patrones_detectados', [])
        }
        self.informes.append(informe)
        logger.info(f"Informe generado para {informe['usuario']}")
        return informe
    
    def guardar_informe(self, informe, nombre_archivo=None):
        try:
            if nombre_archivo is None:
                nombre_archivo = f"informe_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            
            ruta_completa = os.path.join(self.carpeta_informes, nombre_archivo)
            
            with open(ruta_completa, 'w', encoding='utf-8') as f:
                f.write("="*70 + "\n")
                f.write(" INFORME DE EVALUACIÓN - IA GENERALIZADA\n")
                f.write("="*70 + "\n\n")
                
                # Sección 1: Datos básicos
                f.write("DATOS BÁSICOS\n")
                f.write("-"*50 + "\n")
                f.write(f"Fecha: {informe['fecha']}\n")
                f.write(f"Usuario: {informe['usuario']}\n")
                f.write(f"Actividad: {informe['actividad']}\n")
                f.write(f"Tipo: {informe['tipo_actividad']}\n")
                f.write(f"Nivel Usuario: {informe['nivel_usuario']}\n")
                f.write(f"Nivel Requerido: {informe['nivel_requerido']}\n\n")
                
                # Sección 2: Resultado de IA
                f.write("ANÁLISIS DE IA GENERALIZADA\n")
                f.write("-"*50 + "\n")
                f.write(f"Resultado: {informe['resultado'].upper()}\n")
                f.write(f"Recomendación: {informe['recomendacion']}\n")
                f.write(f"Brecha de habilidades: {informe['brecha_habilidades']}\n")
                f.write(f"Confianza del análisis: {informe['confianza_ia']:.2%}\n\n")
                
                # Sección 3: Patrones detectados
                f.write("PATRONES DETECTADOS\n")
                f.write("-"*50 + "\n")
                if informe['patrones_detectados']:
                    for patron in informe['patrones_detectados']:
                        f.write(f"• {patron}\n")
                else:
                    f.write("No se detectaron patrones específicos\n")
                f.write("\n")
                
                # Sección 4: Recomendaciones adicionales
                f.write("RECOMENDACIONES ADICIONALES\n")
                f.write("-"*50 + "\n")
                if informe['acepta_consejos']:
                    f.write("El usuario acepta consejos personalizados\n")
                    f.write(f"{informe.get('analisis_ia', {}).get('recomendacion', '')}\n")
                else:
                    f.write("El usuario no acepta consejos personalizados\n")
                
                f.write("\n" + "="*70 + "\n")
                f.write("Fin del informe\n")
            
            logger.info(f"Informe guardado en: {ruta_completa}")
            return ruta_completa
            
        except Exception as e:
            logger.error(f"Error guardando informe: {str(e)}")
            raise
# Configuraciones del sistema
import os

# Niveles de evaluación
NIVELES = {
    'BASICO': 'básico',
    'INTERMEDIO': 'intermedio', 
    'AVANZADO': 'avanzado'
}

TIPOS_ACTIVIDAD = {
    'TALLER': 'taller',
    'CLUBER': 'cluber'
}

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RUTAS = {
    'ACTIVIDADES': os.path.join(BASE_DIR, 'data', 'actividades.json'),
    'USUARIOS': os.path.join(BASE_DIR, 'data', 'usuarios.json'),
    'INFORMES': os.path.join(BASE_DIR, 'informes'),
    'LOGS': os.path.join(BASE_DIR, 'logs'),
    'DATABASE': os.path.join(BASE_DIR, 'database', 'sistema.db')
}

# Configuración de IA
CONFIANZA_MINIMA = 0.70
CONFIANZA_MAXIMA = 0.95

# Logs
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Crear directorios necesarios
for ruta in [RUTAS['INFORMES'], RUTAS['LOGS']]:
    os.makedirs(ruta, exist_ok=True)
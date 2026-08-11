from datetime import datetime

class Evaluacion:
    def __init__(self, usuario, actividad, puntaje=None):
        self.usuario = usuario
        self.actividad = actividad
        self.puntaje = puntaje
        self.nivel_usuario = None
        self.resultado = None
        self.recomendacion = None
        self.fecha = datetime.now()
        self.confianza_ia = None
    
    def evaluar_nivel(self, puntaje):
        """Evalúa el nivel del usuario basado en el puntaje"""
        if puntaje < 60:
            self.nivel_usuario = 'básico'
        elif 60 <= puntaje < 80:
            self.nivel_usuario = 'intermedio'
        else:
            self.nivel_usuario = 'avanzado'
        self.puntaje = puntaje
        return self.nivel_usuario
    
    def generar_resultado(self):
        """Genera el resultado de la evaluación"""
        if self.nivel_usuario == self.actividad.nivel_requerido:
            self.resultado = 'aprobado'
            self.recomendacion = 'Acceder a la actividad'
        elif self.nivel_usuario == 'avanzado' and self.actividad.nivel_requerido == 'intermedio':
            self.resultado = 'aprobado_sobrecalificado'
            self.recomendacion = 'Acceder a la actividad como mentor'
        else:
            self.resultado = 'no_aprobado'
            if self.nivel_usuario == 'básico' and self.actividad.nivel_requerido == 'avanzado':
                self.recomendacion = 'Se requiere preparación extensiva'
            else:
                self.recomendacion = 'Mejorar nivel antes de acceder'
        return self.resultado
    
    def to_dict(self):
        return {
            'usuario': self.usuario.nombre if hasattr(self.usuario, 'nombre') else self.usuario,
            'actividad': self.actividad.nombre if hasattr(self.actividad, 'nombre') else self.actividad,
            'puntaje': self.puntaje,
            'nivel_usuario': self.nivel_usuario,
            'nivel_requerido': self.actividad.nivel_requerido,
            'resultado': self.resultado,
            'recomendacion': self.recomendacion,
            'fecha': self.fecha.isoformat(),
            'confianza_ia': self.confianza_ia
        }
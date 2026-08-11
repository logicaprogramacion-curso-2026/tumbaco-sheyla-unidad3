class Usuario:
    def __init__(self, nombre, nivel=None, id=None):
        self.id = id
        self.nombre = nombre
        self.nivel = nivel
        self.historial_evaluaciones = []
    
    def agregar_evaluacion(self, evaluacion):
        self.historial_evaluaciones.append(evaluacion)
    
    def obtener_nivel_promedio(self):
        if not self.historial_evaluaciones:
            return None
        
        niveles = {'básico': 1, 'intermedio': 2, 'avanzado': 3}
        total = sum(niveles.get(eval.nivel_usuario, 0) 
                   for eval in self.historial_evaluaciones)
        promedio = total / len(self.historial_evaluaciones)
        
        if promedio <= 1.5:
            return 'básico'
        elif promedio <= 2.5:
            return 'intermedio'
        else:
            return 'avanzado'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nivel': self.nivel,
            'total_evaluaciones': len(self.historial_evaluaciones)
        }
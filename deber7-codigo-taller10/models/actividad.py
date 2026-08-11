class Actividad:
    def __init__(self, id=None, nombre=None, tipo=None, nivel_requerido=None, acepta_consejos=None):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.nivel_requerido = nivel_requerido
        self.acepta_consejos = acepta_consejos
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'nivel_requerido': self.nivel_requerido,
            'acepta_consejos': self.acepta_consejos
        }
    
    def es_accesible(self, nivel_usuario):
        niveles = {'básico': 1, 'intermedio': 2, 'avanzado': 3}
        return niveles.get(nivel_usuario, 0) >= niveles.get(self.nivel_requerido, 0)
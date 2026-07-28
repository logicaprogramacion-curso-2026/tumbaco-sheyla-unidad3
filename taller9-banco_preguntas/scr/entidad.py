class Pregunta:
    def __init__(self, id, pregunta, opcion_a, opcion_b, opcion_c, opcion_d,
                 respuesta_correcta, dificultad, tema):
        self.id = id
        self.pregunta = pregunta
        self.opcion_a = opcion_a
        self.opcion_b = opcion_b
        self.opcion_c = opcion_c
        self.opcion_d = opcion_d
        self.respuesta_correcta = respuesta_correcta
        self.dificultad = dificultad
        self.tema = tema
    
    def to_dict(self):
        return {
            'id': self.id,
            'pregunta': self.pregunta,
            'opcion_a': self.opcion_a,
            'opcion_b': self.opcion_b,
            'opcion_c': self.opcion_c,
            'opcion_d': self.opcion_d,
            'respuesta_correcta': self.respuesta_correcta,
            'dificultad': self.dificultad,
            'tema': self.tema
        }
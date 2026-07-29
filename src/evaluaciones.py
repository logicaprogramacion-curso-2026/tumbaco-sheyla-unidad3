class Evaluacion:
    """
    Clase que representa una evaluación con las notas de los profesores.

    """
    
    def __init__(self, nota_profesor1=0, nota_profesor2=0, autoevaluacion=0):
        """
        Constructor de la clase Evaluacion.
        
        Args:
            nota_profesor1 (int): Nota del profesor 1
            nota_profesor2 (int): Nota del profesor 2
            autoevaluacion (int): Nota de autoevaluación
        """
        self.nota_profesor1 = nota_profesor1
        self.nota_profesor2 = nota_profesor2
        self.autoevaluacion = autoevaluacion
    
    def obtener_notas(self):
        """Retorna las tres notas como una lista."""
        return [self.nota_profesor1, self.nota_profesor2, self.autoevaluacion]
    
    def __str__(self):
        """Representación en string de la evaluación."""
        return f"P1={self.nota_profesor1}, P2={self.nota_profesor2}, Auto={self.autoevaluacion}"
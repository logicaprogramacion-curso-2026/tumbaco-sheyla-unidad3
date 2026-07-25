class Estudiante:
    """
    Clase que representa a un estudiante.
    
    """
    
    def __init__(self, nombre, id=None):
        """
        Constructor de la clase Estudiante.
        
        Args:
            nombre (str): Nombre del estudiante
            id (int, optional): ID del estudiante. Defaults to None.
        """
        self.id = id
        self.nombre = nombre
        self.evaluacion = None # Aquí se almacenará su evaluación
    
    def __str__(self):
        """Representación en string del estudiante."""
        return f"Estudiante: {self.nombre}"
    
    def __eq__(self, other):
        """Compara dos estudiantes por su nombre."""
        if isinstance(other, Estudiante):
            return self.nombre == other.nombre
        return False

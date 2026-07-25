import random
from src.models.estudiante import Estudiante
from src.models.evaluacion import Evaluacion

class GestionEvaluacion:
    """
    Clase que gestiona las evaluaciones de los estudiantes.
    Contiene métodos para asignar parejas, mostrar fechas de entrega, calcular diferencias y verificar acuerdos
   
    """
    
    def __init__(self):
        # ============================================================
        # DATOS 
        # ============================================================
        self.estudiantes = []
        self.datos_evaluaciones = {}
        self.fechas_entregas = ["Tarea 1: 20/06/2026", "Tarea 2: 27/06/2026", "Proyecto: 10/07/2026"]
        self._cargar_datos_prueba()
    
    def _cargar_datos_prueba(self):
        nombres = ["Ana", "Luis", "Carla", "David", "Elena"]
        for nombre in nombres:
            estudiante = Estudiante(nombre)
            self.estudiantes.append(estudiante)
    
        # [nota_profesor1, nota_profesor2, autoevaluacion]
        evaluaciones_originales = {
            "Ana": [85, 90, 88],
            "Luis": [42, 45, 50],
            "Carla": [78, 80, 79],
            "David": [91, 70, 80],
            "Elena": [88, 89, 90]
        }
        
        # Asignar evaluaciones a cada estudiante
        for estudiante in self.estudiantes:
            if estudiante.nombre in evaluaciones_originales:
                notas = evaluaciones_originales[estudiante.nombre]
                evaluacion = Evaluacion(notas[0], notas[1], notas[2])
                estudiante.evaluacion = evaluacion
                # Guardar en el diccionario para compatibilidad
                self.datos_evaluaciones[estudiante.nombre] = [notas[0], notas[1], notas[2]]
    
    def obtener_lista_nombres(self):
        """
        Retorna la lista de nombres de estudiantes.

        """
        return [est.nombre for est in self.estudiantes]
    
    def obtener_evaluaciones_dict(self):
        """
        Retorna el diccionario de evaluaciones.

        """
        return self.datos_evaluaciones.copy()
    
# Esto significa que vamos a usar las funciones de la clase GestionEvaluacion para manejar la lógica de nuestro programa, como asignar parejas, mostrar fechas, calcular diferencias y verificar acuerdos entre evaluadores.
    def asignar_pares(self, lista):
        """
        Asigna pares de estudiantes.
        
        Args:
            lista (list): Lista de nombres de estudiantes
            
        Returns:
            list: Lista de tuplas con las parejas
        """
        pares = []
        cantidad = len(lista)
        for i in range(0, cantidad, 2):
            if i + 1 < cantidad:
                pares.append((lista[i], lista[i + 1]))
            else:
                pares.append((lista[i], "Sin par"))
        return pares
    
    def mostrar_fechas(self):
        """
        Muestra las fechas de entrega.

        """
        print(" * Tarea 1: 20/06/2026")
        print(" * Tarea 2: 27/06/2026")
        print(" * Proyecto: 10/07/2026")
    
    def calcular_diferencia(self, n1, n2, n3):
        """
        Calcula la diferencia entre las notas.
        
        Args:
            n1, n2, n3 (int): Las tres notas
            
        Returns:
            int: Diferencia porcentual
        """
        # Sacar la nota más alta
        if n1 >= n2 and n1 >= n3:
            mayor = n1
        elif n2 >= n1 and n2 >= n3:
            mayor = n2
        else:
            mayor = n3
        
        # Sacar la nota más baja
        if n1 <= n2 and n1 <= n3:
            menor = n1
        elif n2 <= n1 and n2 <= n3:
            menor = n2
        else:
            menor = n3
        
        if mayor == 0:
            return 0
        
        diferencia = ((mayor - menor) * 100) // mayor
        return diferencia
    
    def estan_de_acuerdo(self, n1, n2, n3):
        """
        Verifica si los evaluadores están de acuerdo.
        
        Args:
            n1, n2, n3 (int): Las tres notas
            
        Returns:
            str: "Están de acuerdo" o "No están de acuerdo"
        """
        diferencia = self.calcular_diferencia(n1, n2, n3)
        
        if diferencia <= 20:
            return "Están de acuerdo"
        else:
            return "No están de acuerdo"
    
    def calcular_nota_final(self, n1, n2, n3):
        """
        Calcula la nota final con ponderación.
        
        Args:
            n1, n2, n3 (int): Las tres notas
            
        Returns:
            int: Nota final
        """
        # Los profesores cuentan 40% cada uno, autoevaluación 20%
        nota = (n1 * 40 + n2 * 40 + n3 * 20) // 100
        return nota
    
#Esto va a permitir que el sistema genere parejas aleatorias de estudiantes, obtenga información sobre las evaluaciones y calcule las notas finales de manera organizada y eficiente.
    def obtener_parejas_aleatorias(self):
        """
        Obtiene parejas aleatorias de estudiantes.
        
        Returns:
            list: Lista de parejas
        """
        nombres = self.obtener_lista_nombres()
        copia = nombres.copy()
        random.shuffle(copia)
        return self.asignar_pares(copia)
    
    def obtener_informacion_evaluaciones(self):
        """
        Obtiene la información de todas las evaluaciones.
        
        Returns:
            list: Lista de tuplas (nombre, notas, resultado_acuerdo)
        """
        resultado = []
        for estudiante in self.estudiantes:
            if estudiante.evaluacion:
                notas = estudiante.evaluacion.obtener_notas()
                acuerdo = self.estan_de_acuerdo(notas[0], notas[1], notas[2])
                resultado.append((estudiante.nombre, notas, acuerdo))
        return resultado
    
    def obtener_notas_finales(self):
        """
        Obtiene las notas finales de todos los estudiantes.
        
        Returns:
            list: Lista de tuplas (nombre, nota_final)
        """
        resultado = []
        for estudiante in self.estudiantes:
            if estudiante.evaluacion:
                notas = estudiante.evaluacion.obtener_notas()
                nota_final = self.calcular_nota_final(notas[0], notas[1], notas[2])
                resultado.append((estudiante.nombre, nota_final))
        return resultado

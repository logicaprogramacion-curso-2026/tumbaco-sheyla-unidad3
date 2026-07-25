# Punto de entrada del programa
# Reemplaza este archivo con tu código (o usa el lenguaje que corresponda al curso)
# PROYECTO GRUPO 7 - Lógica de Programación - AUTOMATIZACIÓN DE LOGÍSTICA Y COHERENCIA
import random
from src.services.gestion_evaluacion import GestionEvaluacion

# ============================================================
# INICIALIZACIÓN
# ============================================================
sistema = GestionEvaluacion()
estudiantes = sistema.obtener_lista_nombres()
evaluaciones = sistema.obtener_evaluaciones_dict()

# ============================================================
# MENÚ - (con pequeños ajustes para usar las clases)
# ============================================================

print("\n" + "=" * 45)
print("SISTEMA DE COORDINACIÓN DOCENTE")
print("=" * 45)
print(" Grupo 7 - Lógica de Programación")
print("=" * 45)

while True:
    print("\n" + "-" * 35)
    print(" 1 → Hacer parejas al azar")
    print(" 2 → Ver fechas de entrega")
    print(" 3 → Ver si los profesores están de acuerdo")
    print(" 4 → Calcular nota final del estudiante")
    print(" 5 → Salir")
    print("-" * 35)
    
    opcion = input(" ➤ Elige: ")
    
    match opcion:
        case "1":
            print("\n HACIENDO PAREJAS...")
            copia = estudiantes.copy()
            random.shuffle(copia)
            pares = sistema.asignar_pares(copia) # TU función original
            
            print("\n PAREJAS:")
            for p in pares:
                print(f" {p[0]} ↔ {p[1]}")
        
        case "2":
            print("\n FECHAS DE ENTREGA:")
            sistema.mostrar_fechas() # TU función original
        
        case "3":
            print("\n VERIFICANDO...")
            print(" (Máx 20% de diferencia para estar de acuerdo)")
            print(" " + "-" * 35)
            
            for nombre in estudiantes:
                notas = evaluaciones[nombre]
                resultado = sistema.estan_de_acuerdo(notas[0], notas[1], notas[2]) # TU función original
                print(f" {nombre}: {notas[0]}/{notas[1]}/{notas[2]} → {resultado}")
        
        case "4":
            print("\n NOTA FINAL:")
            print(" (Cada profesor 40% | Autoevaluación 20%)")
            print(" " + "-" * 30)
            
            for nombre in estudiantes:
                notas = evaluaciones[nombre]
                nota_final = sistema.calcular_nota_final(notas[0], notas[1], notas[2]) # TU función original
                print(f" {nombre}: {nota_final} puntos")
        
        case "5":
            print("\n ¡Hasta luego!")
            break
        
        case _:
            print(" Opción no válida. Elige 1,2,3,4 o 5.")

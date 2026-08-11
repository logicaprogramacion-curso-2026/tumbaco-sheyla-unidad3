from models.actividad import Actividad
from models.usuario import Usuario
from services.evaluador import EvaluadorActividades
from utils.validadores import validar_puntaje, formatear_mensaje
import json
import os

def cargar_actividades():
    """Carga actividades desde archivo JSON"""
    try:
        with open('data/actividades.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Actividad(**act) for act in data['actividades']]
    except FileNotFoundError:
        # Actividades por defecto
        return [
            Actividad("Taller de Programación", "taller", "intermedio"),
            Actividad("Cluber de Robótica", "cluber", "avanzado"),
            Actividad("Taller de Diseño", "taller", "básico")
        ]

def mostrar_menu():
    print("\n" + "="*50)
    print(" SISTEMA DE EVALUACIÓN CON IA GENERALIZADA")
    print("="*50)
    print("1. Evaluar nuevo usuario")
    print("2. Ver estadísticas de IA")
    print("3. Ver historial de análisis")
    print("4. Ver informes guardados")
    print("5. Salir")
    print("="*50)
    return input("Seleccione una opción: ")

def main():
    evaluador = EvaluadorActividades()
    actividades = cargar_actividades()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            # Mostrar actividades disponibles
            print("\n Actividades disponibles:")
            for i, act in enumerate(actividades, 1):
                print(f"{i}. {act.nombre} ({act.tipo}) - Nivel: {act.nivel_requerido}")
            
            try:
                seleccion = int(input("\nSeleccione número de actividad: ")) - 1
                if 0 <= seleccion < len(actividades):
                    actividad = actividades[seleccion]
                    
                    nombre_usuario = input("Nombre del usuario: ")
                    usuario = Usuario(nombre_usuario)
                    
                    # Validar puntaje
                    while True:
                        try:
                            puntaje = float(input("Puntaje obtenido (0-100): "))
                            if validar_puntaje(puntaje):
                                break
                            print("Puntaje inválido. Debe ser entre 0 y 100.")
                        except ValueError:
                            print("Ingrese un número válido")
                    
                    print("\n" + "="*50)
                    print("Procesando evaluación con IA Generalizada...")
                    resultado = evaluador.procesar_evaluacion(usuario, actividad, puntaje)
                    
                    # Mostrar resultados
                    print("\n EVALUACIÓN COMPLETADA")
                    print("="*50)
                    print(f"Usuario: {resultado['analisis']['usuario']}")
                    print(f"Actividad: {resultado['analisis']['actividad']}")
                    print(f"Nivel: {resultado['analisis']['nivel_usuario']}")
                    print(f"Resultado: {resultado['analisis']['resultado']}")
                    print(f"Recomendación IA: {resultado['analisis']['recomendacion']}")
                    print(f"Confianza IA: {resultado['analisis']['confianza_analisis']:.2%}")
                    
                    # Guardar informe
                    archivo = evaluador.generador_informe.guardar_informe(resultado['informe'])
                    print(f"\n Informe guardado: {archivo}")
                    
                else:
                    print("❌ Selección inválida")
            except ValueError:
                print("❌ Ingrese un número válido")
            
        elif opcion == "2":
            print("\n ESTADÍSTICAS DE IA GENERALIZADA")
            print("="*50)
            stats = evaluador.obtener_estadisticas_ia()
            if isinstance(stats, dict):
                for key, value in stats.items():
                    if key == 'distribucion_niveles':
                        print(f"\n Distribución de niveles:")
                        for nivel, count in value.items():
                            print(f" {nivel}: {count} usuarios")
                    else:
                        print(f"{key}: {value}")
            else:
                print(stats)
            
        elif opcion == "3":
            print("\n HISTORIAL DE ANÁLISIS")
            print("="*50)
            if evaluador.ia.historial_analisis:
                for i, analisis in enumerate(evaluador.ia.historial_analisis, 1):
                    print(f"\n--- Análisis #{i} ---")
                    print(f"Usuario: {analisis['usuario']}")
                    print(f"Actividad: {analisis['actividad']}")
                    print(f"Resultado: {analisis['resultado']}")
                    print(f"Confianza: {analisis['confianza_analisis']:.2%}")
            else:
                print("No hay análisis en el historial")
            
        elif opcion == "4":
            print("\n INFORMES GUARDADOS")
            print("="*50)
            import os
            from config.settings import RUTAS
            
            if os.path.exists(RUTAS['INFORMES']):
                informes = os.listdir(RUTAS['INFORMES'])
                if informes:
                    for i, inf in enumerate(informes, 1):
                        print(f"{i}. {inf}")
                    try:
                        sel = int(input("\nSeleccione informe para ver: ")) - 1
                        if 0 <= sel < len(informes):
                            with open(os.path.join(RUTAS['INFORMES'], informes[sel]), 'r', encoding='utf-8') as f:
                                print("\n" + f.read())
                        else:
                            print("Selección inválida")
                    except ValueError:
                        print("Ingrese un número válido")
                else:
                    print("No hay informes guardados")
            else:
                print("No hay informes guardados")
            
        elif opcion == "5":
            print("\n ¡Hasta luego!")
            break
        
        else:
            print("Opción inválida")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()

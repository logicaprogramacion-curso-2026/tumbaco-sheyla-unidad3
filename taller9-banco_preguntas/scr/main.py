from gestor import GestorPreguntas
from simulador import Simulador
from dao import PreguntaDAO
import os

def mostrar_menu():
    print("\n" + "=" * 50)
    print("SISTEMA DE BANCO DE PREGUNTAS")
    print("=" * 50)
    print(" 1 -> Cargar preguntas desde archivo")
    print(" 2 -> Ver todas las preguntas")
    print(" 3 -> Ver estadisticas")
    print(" 4 -> Iniciar simulacion")
    print(" 5 -> Exportar datos")
    print(" 6 -> Ver reportes")
    print(" 7 -> Salir")
    print("-" * 50)

def main():
    gestor = GestorPreguntas()
    dao = PreguntaDAO()
    simulador = Simulador()
    
    # Garantizar que la tabla exista en SQLite desde el inicio
    try:
        dao.crear_tabla()
    except Exception as e:
        pass
    
    while True:
        mostrar_menu()
        opcion = input(" Elige: ")
        
        if opcion == "1":
            print("\nCARGAR PREGUNTAS")
            print(" 1 -> Desde TXT")
            print(" 2 -> Desde CSV")
            print(" 3 -> Desde JSON")
            sub = input(" Elige: ")
            try:
                if sub == "1":
                    preguntas = gestor.cargar_desde_txt('preguntas.txt')
                elif sub == "2":
                    preguntas = gestor.cargar_desde_csv('preguntas.csv')
                elif sub == "3":
                    preguntas = gestor.cargar_desde_json('preguntas.json')
                else:
                    print("Opcion invalida")
                    input("\nPresiona Enter para continuar...")
                    continue
                
                print(f"\n {len(preguntas)} preguntas cargadas desde el archivo.")
                guardar = input("¿Guardar en la base de datos? (s/n): ")
                if guardar.lower() == 's':
                    gestor.guardar_en_base_datos(preguntas)
                    print("Preguntas guardadas con éxito en la base de datos SQLite.")
            except FileNotFoundError as e:
                print(f"Archivo no encontrado: {e}")
            except Exception as e:
                print(f"Error al cargar: {e}")
            
            input("\nPresiona Enter para volver al menu...")
        
        elif opcion == "2":
            preguntas = dao.obtener_todas()
            if not preguntas:
                print("\n No hay preguntas en la base de datos.")
                print("Pista: Usa la Opcion 1 para cargar preguntas y presiona 's' para guardarlas en la BD.")
            else:
                print(f"\n--- TOTAL EN BD: {len(preguntas)} preguntas ---")
                for p in preguntas[:10]:
                    # Soporta si 'p' es un objeto o una tupla de SQLite
                    p_id = getattr(p, 'id', p[0] if isinstance(p, (tuple, list)) else 'N/A')
                    p_txt = getattr(p, 'pregunta', p[1] if isinstance(p, (tuple, list)) else 'N/A')
                    p_dif = getattr(p, 'dificultad', p[7] if isinstance(p, (tuple, list)) else 'N/A')
                    print(f" [{p_id}] {str(p_txt)[:60]}... ({p_dif})")
                
                if len(preguntas) > 10:
                    print(f" ... y {len(preguntas)-10} preguntas más.")
            
            # Pausa obligatoria para que el usuario pueda leer la información
            input("\nPresiona Enter para volver al menu...")
        
        elif opcion == "3":
            stats = dao.estadisticas_por_tema()
            total = dao.contar_preguntas()
            print(f"\nTOTAL PREGUNTAS EN BD: {total}")
            if stats:
                print("\nPOR TEMA:")
                for fila in stats:
                    print(f" {fila}")
            else:
                print("No hay datos estadisticos disponibles.")
            
            input("\nPresiona Enter para volver al menu...")
        
        elif opcion == "4":
            try:
                cantidad = int(input("¿Cuántas preguntas deseas en la simulación? (max 50): "))
                if cantidad > 50:
                    cantidad = 50
                simulador.iniciar_simulacion(cantidad)
            except ValueError:
                print("Ingresa un número válido")
            
            input("\nPresiona Enter para volver al menu...")
        
        elif opcion == "5":
            os.makedirs('resultados', exist_ok=True)
            print("\nEXPORTAR DATOS")
            print(" 1 -> Exportar a TXT")
            print(" 2 -> Exportar a CSV")
            print(" 3 -> Exportar a JSON")
            sub = input(" Elige: ")
            
            preguntas = dao.obtener_todas()
            if not preguntas:
                print("No hay preguntas en la base de datos para exportar")
            else:
                if sub == "1":
                    gestor.exportar_a_txt('resultados/exportacion.txt', preguntas)
                elif sub == "2":
                    gestor.exportar_a_csv('resultados/exportacion.csv', preguntas)
                elif sub == "3":
                    gestor.exportar_a_json('resultados/exportacion.json', preguntas)
                else:
                    print("Opcion invalida")
                print("Exportación completada en la carpeta 'resultados/'")
            
            input("\nPresiona Enter para volver al menu...")
        
        elif opcion == "6":
            if os.path.exists('resultados'):
                archivos = os.listdir('resultados')
                if archivos:
                    print("\nREPORTES DISPONIBLES EN 'resultados/':")
                    for archivo in archivos:
                        print(f" {archivo}")
                else:
                    print("No hay archivos en la carpeta resultados/")
            else:
                print("No se encuentra la carpeta resultados/")
            
            input("\nPresiona Enter para volver al menu...")
        
        elif opcion == "7":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción inválida")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()



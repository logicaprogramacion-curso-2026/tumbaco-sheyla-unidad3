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

    try:
        dao.crear_tabla()
    except Exception:
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
                    preguntas = gestor.cargar_desde_txt("preguntas.txt")

                elif sub == "2":
                    preguntas = gestor.cargar_desde_csv("preguntas.csv")

                elif sub == "3":
                    preguntas = gestor.cargar_desde_json("preguntas.json")

                else:
                    print("Opción inválida")
                    input("\nPresiona Enter para continuar...")
                    continue

                print(f"\n{len(preguntas)} preguntas cargadas desde el archivo.")

                guardar = input("¿Guardar en la base de datos? (s/n): ")

                if guardar.lower() == "s":
                    gestor.guardar_en_base_datos(preguntas)
                    print("Preguntas guardadas con éxito en SQLite.")

            except FileNotFoundError as e:
                print(f"Archivo no encontrado: {e}")

            except Exception as e:
                print(f"Error al cargar: {e}")

            input("\nPresiona Enter para volver al menú...")

        elif opcion == "2":
            preguntas = dao.obtener_todas()

            if not preguntas:
                print("\nNo hay preguntas en la base de datos.")
            else:
                print(f"\nTOTAL: {len(preguntas)} preguntas")

                for p in preguntas[:10]:
                    p_id = getattr(p, "id", p[0] if isinstance(p, (tuple, list)) else "")
                    p_txt = getattr(p, "pregunta", p[1] if isinstance(p, (tuple, list)) else "")
                    p_dif = getattr(p, "dificultad", p[7] if isinstance(p, (tuple, list)) else "")

                    print(f"[{p_id}] {p_txt} ({p_dif})")

                if len(preguntas) > 10:
                    print(f"... y {len(preguntas)-10} preguntas más.")

            input("\nPresiona Enter para volver al menú...")

        elif opcion == "3":
            print(f"\nTOTAL: {dao.contar_preguntas()}")

            for fila in dao.estadisticas_por_tema():
                print(fila)

            input("\nPresiona Enter para volver al menú...")

        elif opcion == "4":
            try:
                cantidad = int(input("Cantidad de preguntas (máx. 50): "))

                if cantidad > 50:
                    cantidad = 50

                simulador.iniciar_simulacion(cantidad)

            except ValueError:
                print("Número inválido")

            input("\nPresiona Enter para volver al menú...")

        elif opcion == "5":

            os.makedirs("resultados", exist_ok=True)

            preguntas = dao.obtener_todas()

            if not preguntas:
                print("No hay preguntas para exportar.")

            else:
                print("\n1 -> TXT")
                print("2 -> CSV")
                print("3 -> JSON")

                sub = input("Elige: ")

                if sub == "1":
                    gestor.exportar_a_txt("resultados/exportacion.txt", preguntas)

                elif sub == "2":
                    gestor.exportar_a_csv("resultados/exportacion.csv", preguntas)

                elif sub == "3":
                    gestor.exportar_a_json("resultados/exportacion.json", preguntas)

                print("Exportación completada.")

            input("\nPresiona Enter para volver al menú...")

        elif opcion == "6":

            if os.path.exists("resultados"):

                archivos = os.listdir("resultados")

                if archivos:
                    print("\nREPORTES:")
                    for archivo in archivos:
                        print(archivo)
                else:
                    print("No hay reportes.")

            else:
                print("No existe la carpeta resultados.")

            input("\nPresiona Enter para volver al menú...")

        elif opcion == "7":
            print("\n¡Hasta luego!")
            break

        else:
            print("Opción inválida")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()

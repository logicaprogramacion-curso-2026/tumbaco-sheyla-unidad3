import json
import csv
import random
import os
from datetime import datetime
from dao import PreguntaDAO

class Simulador:
    def __init__(self):
        self.dao = PreguntaDAO()

    def iniciar_simulacion(self, cantidad):
        preguntas = self.dao.obtener_todas()
        if not preguntas:
            print("\n No hay preguntas en la base de datos para la simulación.")
            return

        if len(preguntas) < cantidad:
            cantidad = len(preguntas)

        preguntas_seleccionadas = random.sample(preguntas, cantidad)
        respuestas_usuario = []
        correctas = 0

        print("\n" + "=" * 50)
        print("SIMULADOR DE EVALUACIÓN")
        print("=" * 50)

        for i, p in enumerate(preguntas_seleccionadas, 1):
            if hasattr(p, 'id'):
                p_id, preg, a, b, c, d, resp, dif, tema = p.id, p.pregunta, p.opcion_a, p.opcion_b, p.opcion_c, p.opcion_d, p.respuesta_correcta, p.dificultad, p.tema
            else:
                p_id, preg, a, b, c, d, resp, dif, tema = p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]

            print(f"\nPregunta {i} ({dif} - {tema})")
            print(f"{preg}")
            print(f"A) {a}")
            print(f"B) {b}")
            print(f"C) {c}")
            print(f"D) {d}")

            ans = input("► Tu respuesta (A/B/C/D): ").strip().upper()
            es_correcta = (ans == resp.strip().upper())

            if es_correcta:
                print("¡Correcto!")
                correctas += 1
            else:
                print(f"Incorrecto. La respuesta correcta era: {resp}")

            respuestas_usuario.append({
                "id": p_id,
                "pregunta": preg,
                "respuesta_usuario": ans,
                "respuesta_correcta": resp,
                "es_correcta": es_correcta,
                "tema": tema,
                "dificultad": dif
            })

        puntaje = (correctas / cantidad) * 10
        print("\n" + "=" * 50)
        print("SIMULACIÓN FINALIZADA")
        print(f"Puntaje obtenido: {puntaje:.2f} / 10 ({correctas} de {cantidad} correctas)")
        print("=" * 50)

        # Escribir físicamente los 3 reportes en resultados/
        self.generar_reportes(respuestas_usuario, puntaje, cantidad, correctas)

    def generar_reportes(self, respuestas, puntaje, total, correctas):
        os.makedirs('resultados', exist_ok=True)
        fecha_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 1. Escribir respuestas_usuario.txt
        with open('resultados/respuestas_usuario.txt', 'w', encoding='utf-8') as f:
            f.write(f"REPORTE DE SIMULACION - {fecha_str}\n")
            f.write(f"Puntaje: {puntaje:.2f}/10 ({correctas}/{total} correctas)\n")
            f.write("=" * 50 + "\n\n")
            for r in respuestas:
                estado = "CORRECTO" if r['es_correcta'] else "INCORRECTO"
                f.write(f"[{estado}] ID {r['id']}: {r['pregunta']}\n")
                f.write(f" Tu respuesta: {r['respuesta_usuario']} | Correcta: {r['respuesta_correcta']}\n\n")

        # 2. Escribir reporte.json
        reporte_json_data = {
            "fecha": fecha_str,
            "total_preguntas": total,
            "correctas": correctas,
            "puntaje": round(puntaje, 2),
            "detalle_respuestas": respuestas
        }
        with open('resultados/reporte.json', 'w', encoding='utf-8') as f:
            json.dump(reporte_json_data, f, indent=4, ensure_ascii=False)

        # 3. Escribir estadisticas.csv
        with open('resultados/estadisticas.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Metrica", "Valor"])
            writer.writerow(["Fecha", fecha_str])
            writer.writerow(["Total Preguntas", total])
            writer.writerow(["Respuestas Correctas", correctas])
            writer.writerow(["Puntaje Final", f"{puntaje:.2f}"])
        
        print("Reportes generados exitosamente con datos dentro de 'resultados/'")


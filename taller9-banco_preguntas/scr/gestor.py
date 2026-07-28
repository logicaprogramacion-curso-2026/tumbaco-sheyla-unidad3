import json
import csv
import json
import os

class GestorPreguntas:
    def __init__(self):
        pass

    # ... conserva tus métodos de cargar_desde_txt, csv y json ...

    def exportar_a_txt(self, ruta, preguntas):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as f:
            for p in preguntas:
                if hasattr(p, 'pregunta'):
                    f.write(f"ID: {p.id}\nPregunta: {p.pregunta}\nA) {p.opcion_a}\nB) {p.opcion_b}\nC) {p.opcion_c}\nD) {p.opcion_d}\nCorrecta: {p.respuesta_correcta}\nDificultad: {p.dificultad}\nTema: {p.tema}\n{'-'*40}\n")
                else:
                    f.write(f"ID: {p[0]}\nPregunta: {p[1]}\nA) {p[2]}\nB) {p[3]}\nC) {p[4]}\nD) {p[5]}\nCorrecta: {p[6]}\nDificultad: {p[7]}\nTema: {p[8]}\n{'-'*40}\n")

    def exportar_a_csv(self, ruta, preguntas):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'pregunta', 'opcion_a', 'opcion_b', 'opcion_c', 'opcion_d', 'respuesta_correcta', 'dificultad', 'tema'])
            for p in preguntas:
                if hasattr(p, 'pregunta'):
                    writer.writerow([p.id, p.pregunta, p.opcion_a, p.opcion_b, p.opcion_c, p.opcion_d, p.respuesta_correcta, p.dificultad, p.tema])
                else:
                    writer.writerow(list(p))

    def exportar_a_json(self, ruta, preguntas):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        datos = []
        for p in preguntas:
            if hasattr(p, 'to_dict'):
                datos.append(p.to_dict())
            elif hasattr(p, 'pregunta'):
                datos.append({
                    "id": p.id, "pregunta": p.pregunta, "opcion_a": p.opcion_a,
                    "opcion_b": p.opcion_b, "opcion_c": p.opcion_c, "opcion_d": p.opcion_d,
                    "respuesta_correcta": p.respuesta_correcta, "dificultad": p.dificultad, "tema": p.tema
                })
            else:
                datos.append({
                    "id": p[0], "pregunta": p[1], "opcion_a": p[2],
                    "opcion_b": p[3], "opcion_c": p[4], "opcion_d": p[5],
                    "respuesta_correcta": p[6], "dificultad": p[7], "tema": p[8]
                })
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)


import json
import csv
import os

# Carpeta donde está el proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class GestorPreguntas:

    def __init__(self):
        pass

    # ==========================
    # CARGAR DESDE TXT
    # ==========================
    def cargar_desde_txt(self, ruta):
        preguntas = []

        ruta = os.path.join(BASE_DIR, ruta)

        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()

        bloques = contenido.split("-" * 40)

        for bloque in bloques:
            if "Pregunta:" in bloque:
                preguntas.append(bloque.strip())

        return preguntas

    # ==========================
    # CARGAR DESDE CSV
    # ==========================
    def cargar_desde_csv(self, ruta):
        preguntas = []

        ruta = os.path.join(BASE_DIR, ruta)

        with open(ruta, "r", encoding="utf-8") as f:
            lector = csv.reader(f)

            next(lector, None)

            for fila in lector:
                preguntas.append(fila)

        return preguntas

    # ==========================
    # CARGAR DESDE JSON
    # ==========================
    def cargar_desde_json(self, ruta):

        ruta = os.path.join(BASE_DIR, ruta)

        with open(ruta, "r", encoding="utf-8") as f:
            preguntas = json.load(f)

        return preguntas

    # ==========================
    # EXPORTAR A TXT
    # ==========================
    def exportar_a_txt(self, ruta, preguntas):

        os.makedirs(os.path.dirname(ruta), exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as f:

            for p in preguntas:

                if hasattr(p, "pregunta"):

                    f.write(
                        f"ID: {p.id}\n"
                        f"Pregunta: {p.pregunta}\n"
                        f"A) {p.opcion_a}\n"
                        f"B) {p.opcion_b}\n"
                        f"C) {p.opcion_c}\n"
                        f"D) {p.opcion_d}\n"
                        f"Correcta: {p.respuesta_correcta}\n"
                        f"Dificultad: {p.dificultad}\n"
                        f"Tema: {p.tema}\n"
                        f"{'-'*40}\n"
                    )

                else:

                    f.write(
                        f"ID: {p[0]}\n"
                        f"Pregunta: {p[1]}\n"
                        f"A) {p[2]}\n"
                        f"B) {p[3]}\n"
                        f"C) {p[4]}\n"
                        f"D) {p[5]}\n"
                        f"Correcta: {p[6]}\n"
                        f"Dificultad: {p[7]}\n"
                        f"Tema: {p[8]}\n"
                        f"{'-'*40}\n"
                    )

    # ==========================
    # EXPORTAR A CSV
    # ==========================
    def exportar_a_csv(self, ruta, preguntas):

        os.makedirs(os.path.dirname(ruta), exist_ok=True)

        with open(ruta, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                "id",
                "pregunta",
                "opcion_a",
                "opcion_b",
                "opcion_c",
                "opcion_d",
                "respuesta_correcta",
                "dificultad",
                "tema"
            ])

            for p in preguntas:

                if hasattr(p, "pregunta"):

                    writer.writerow([
                        p.id,
                        p.pregunta,
                        p.opcion_a,
                        p.opcion_b,
                        p.opcion_c,
                        p.opcion_d,
                        p.respuesta_correcta,
                        p.dificultad,
                        p.tema
                    ])

                else:
                    writer.writerow(list(p))

    # ==========================
    # EXPORTAR A JSON
    # ==========================
    def exportar_a_json(self, ruta, preguntas):

        os.makedirs(os.path.dirname(ruta), exist_ok=True)

        datos = []

        for p in preguntas:

            if hasattr(p, "to_dict"):
                datos.append(p.to_dict())

            elif hasattr(p, "pregunta"):

                datos.append({
                    "id": p.id,
                    "pregunta": p.pregunta,
                    "opcion_a": p.opcion_a,
                    "opcion_b": p.opcion_b,
                    "opcion_c": p.opcion_c,
                    "opcion_d": p.opcion_d,
                    "respuesta_correcta": p.respuesta_correcta,
                    "dificultad": p.dificultad,
                    "tema": p.tema
                })

            else:

                datos.append({
                    "id": p[0],
                    "pregunta": p[1],
                    "opcion_a": p[2],
                    "opcion_b": p[3],
                    "opcion_c": p[4],
                    "opcion_d": p[5],
                    "respuesta_correcta": p[6],
                    "dificultad": p[7],
                    "tema": p[8]
                })

        with open(ruta, "w", encoding="latin-1") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

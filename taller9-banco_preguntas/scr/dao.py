import sqlite3
import os
from entidad import Pregunta

class PreguntaDAO:
    def __init__(self, db_path="database/preguntas.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path
        self.crear_tabla()
    
    def _get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def crear_tabla(self):
        query = """
        CREATE TABLE IF NOT EXISTS preguntas (
            id INTEGER PRIMARY KEY,
            pregunta TEXT NOT NULL,
            opcion_a TEXT NOT NULL,
            opcion_b TEXT NOT NULL,
            opcion_c TEXT NOT NULL,
            opcion_d TEXT NOT NULL,
            respuesta_correcta TEXT NOT NULL,
            dificultad TEXT NOT NULL,
            tema TEXT NOT NULL
        )
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
    
    def insertar(self, pregunta):
        query = """
        INSERT OR REPLACE INTO preguntas
        (id, pregunta, opcion_a, opcion_b, opcion_c, opcion_d,
         respuesta_correcta, dificultad, tema)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(query, (
            pregunta.id, pregunta.pregunta, pregunta.opcion_a,
            pregunta.opcion_b, pregunta.opcion_c, pregunta.opcion_d,
            pregunta.respuesta_correcta, pregunta.dificultad, pregunta.tema
        ))
        conn.commit()
        conn.close()
    
    def insertar_muchas(self, preguntas):
        for p in preguntas:
            self.insertar(p)
    
    def obtener_todas(self):
        query = "SELECT * FROM preguntas ORDER BY id"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [Pregunta(*row) for row in rows]
    
    def obtener_por_id(self, id):
        query = "SELECT * FROM preguntas WHERE id = ?"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Pregunta(*row)
        return None
    
    def contar_preguntas(self):
        query = "SELECT COUNT(*) FROM preguntas"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        count = cursor.fetchone()[0]
        conn.close()
        return count
    
    def estadisticas_por_tema(self):
        query = """
        SELECT tema, COUNT(*) as total,
               SUM(CASE WHEN dificultad = 'Fácil' THEN 1 ELSE 0 END) as facil,
               SUM(CASE WHEN dificultad = 'Media' THEN 1 ELSE 0 END) as media,
               SUM(CASE WHEN dificultad = 'Difícil' THEN 1 ELSE 0 END) as dificil
        FROM preguntas
        GROUP BY tema
        ORDER BY tema
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows

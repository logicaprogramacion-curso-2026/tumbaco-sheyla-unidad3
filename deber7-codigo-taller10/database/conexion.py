import sqlite3
import os
from config.settings import RUTAS

class DatabaseConnection:
    def __init__(self):
        self.db_path = RUTAS['DATABASE']
        self.conn = None
        self.cursor = None
        self._crear_tablas()
    
    def conectar(self):
        """Establece conexión con la base de datos"""
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def cerrar(self):
        """Cierra la conexión"""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
    
    def _crear_tablas(self):
        """Crea las tablas necesarias si no existen"""
        self.conectar()
        
        # Tabla de usuarios
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                nivel TEXT,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabla de actividades
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS actividades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                tipo TEXT NOT NULL,
                nivel_requerido TEXT NOT NULL,
                acepta_consejos INTEGER DEFAULT 1
            )
        ''')
        
        # Tabla de evaluaciones
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS evaluaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                actividad_id INTEGER,
                puntaje REAL,
                nivel_usuario TEXT,
                resultado TEXT,
                recomendacion TEXT,
                confianza_ia REAL,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY (actividad_id) REFERENCES actividades(id)
            )
        ''')
        
        # Tabla de análisis de IA
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS analisis_ia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                evaluacion_id INTEGER,
                brecha_habilidades TEXT,
                patrones_detectados TEXT,
                detalle_analisis TEXT,
                FOREIGN KEY (evaluacion_id) REFERENCES evaluaciones(id)
            )
        ''')
        
        self.conn.commit()
        self.cerrar()
    
    def ejecutar_consulta(self, query, params=None):
        """Ejecuta una consulta SQL"""
        self.conectar()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()
        return self.cursor
    
    def obtener_datos(self, query, params=None):
        """Obtiene datos de la base de datos"""
        self.conectar()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        datos = self.cursor.fetchall()
        self.cerrar()
        return datos
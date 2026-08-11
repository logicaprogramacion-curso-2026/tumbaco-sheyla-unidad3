-- Esquema de la base de datos

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nivel TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de actividades
CREATE TABLE IF NOT EXISTS actividades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    nivel_requerido TEXT NOT NULL,
    acepta_consejos INTEGER DEFAULT 1
);

-- Tabla de evaluaciones
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
);

-- Tabla de análisis de IA
CREATE TABLE IF NOT EXISTS analisis_ia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evaluacion_id INTEGER,
    brecha_habilidades TEXT,
    patrones_detectados TEXT,
    detalle_analisis TEXT,
    FOREIGN KEY (evaluacion_id) REFERENCES evaluaciones(id)
);

-- Índices para mejorar rendimiento
CREATE INDEX IF NOT EXISTS idx_usuario_nivel ON usuarios(nivel);
CREATE INDEX IF NOT EXISTS idx_evaluacion_fecha ON evaluaciones(fecha);
CREATE INDEX IF NOT EXISTS idx_evaluacion_resultado ON evaluaciones(resultado);
# Sistema de Evaluación de Actividades con IA Generalizada

## Descripción
Sistema inteligente para evaluar y gestionar actividades (talleres y clubers) utilizando IA Generalizada.

## Características de la IA Generalizada
- Análisis de brecha de habilidades
- Recomendaciones personalizadas por nivel
- Detección de patrones de comportamiento
- Cálculo de confianza en el análisis
- Historial de análisis con estadísticas
- Modelo de decisión basado en niveles (básico/intermedio/avanzado)

## Estructura del Proyecto

---

```

deber7-codigo-taller10/
├── .gitignore # Archivos ignorados por Git
├── README.md # Documentación del proyecto
├── requirements.txt # Dependencias del proyecto
├── main.py # Punto de entrada del programa
├── database.py # Conexión a la base de datos
│
├── models/ # Modelos de datos
│ ├── init.py
│ ├── actividad.py # Clase Actividad
│ ├── evaluacion.py # Clase Evaluacion
│ └── usuario.py # Clase Usuario
│
├── services/ # Lógica de negocio e IA
│ ├── init.py
│ ├── ia_generalizada.py # Núcleo de la IA Generalizada
│ ├── evaluador.py # Evaluador de actividades
│ └── generador_informe.py # Generador de informes
│
├── utils/ # Utilidades
│ ├── init.py
│ ├── validadores.py # Validaciones
│ └── helpers.py # Funciones auxiliares
│
├── data/ # Datos de ejemplo
│ ├── actividades.json # Actividades disponibles
│ └── usuarios.json # Usuarios registrados
│
├── tests/ # Pruebas unitarias
│ ├── init.py
│ ├── test_ia_generalizada.py # Pruebas de IA
│ └── test_evaluador.py # Pruebas del evaluador
│
├── database/ # Base de datos
│ ├── init.py
│ ├── conexion.py # Conexión a SQLite
│ ├── esquemas.sql # Esquemas de tablas
│ └── sistema.db # Base de datos SQLite (autogenerada)
│
├── config/ # Configuraciones
│ ├── init.py
│ └── settings.py # Configuración del sistema
│
├── logs/ # Logs del sistema
│ └── app.log # Registro de actividades
│
├── informes/ # Informes generados
│ └── informe_*.txt # Informes de evaluación
│
└── docs/ # Documentación adicional
├── documentacion.md
└── guia_ia.md

```
---

### Flujo del Sistema

1. **Selección de actividad** (taller o cluber)
2. **Ingreso de puntaje** del usuario (0-100)
3. **Evaluación del nivel** (básico/intermedio/avanzado)
4. **Análisis por IA Generalizada**
   - Cálculo de brecha de habilidades
   - Detección de patrones
   - Recomendación personalizada
5. **Generación de informe** en texto
6. **Registro en base de datos** SQLite

---

### Instalación

```bash
# Clonar o ubicarse en la carpeta
cd deber7-codigo-taller10

# Instalar dependencias
pip install -r requirements.txt
```

---

Uso

```bash
# Ejecutar el programa
python main.py
```

Menú principal:

```
==================================================
        SISTEMA DE EVALUACIÓN CON IA GENERALIZADA
==================================================
1. Evaluar nuevo usuario
2. Ver estadísticas de IA
3. Ver historial de análisis
4. Ver informes guardados
5. Salir
==================================================
```

---

Ejemplo de Evaluación

```
Actividades disponibles:
1. Taller de Programación (taller) - Nivel: intermedio
2. Cluber de Robótica (cluber) - Nivel: avanzado
3. Taller de Diseño (taller) - Nivel: básico

Seleccione número de actividad: 1
Nombre del usuario: Sheyla Tumbaco
Puntaje obtenido (0-100): 75

EVALUACIÓN COMPLETADA
Usuario: Sheyla Tumbaco
Actividad: Taller de Programación
Nivel: intermedio
Resultado: aprobado
Recomendación IA: Recomendación: nivel adecuado para profundizar. Practicar con proyectos reales
Confianza IA: 92.00%

Informe guardado: informes/informe_20260811_222004.txt
```

---

Niveles de Evaluación

Puntaje Nivel Descripción
0 - 59 Básico Conocimientos iniciales
60 - 79 Intermedio Conocimientos sólidos
80 - 100 Avanzado Conocimientos expertos

---

Pruebas

```bash
# Ejecutar pruebas unitarias
python -m pytest tests/

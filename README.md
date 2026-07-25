# [AUTOMATIZACIÓN DE LOGÍSTICA Y COHERENCIA]
**Alumno:** [Tumbaco, Sheyla]
# [NTEGRANTES DEL PROYECTO]
---
**DOMENICA BELEN RODRIGUEZ NARANJO**
---
**MAYDELEINE SAMIRA SANCHEZ MONROY**
---
**SHEYLA ARLETTE TUMBACO MORÁN**
---
**Curso:** [Lógica de Programación]
---
**Fecha de inicio:** [12/06/2026]
--- 

## Objetivo del proyecto

Desarrollar un sistema automatizado para la gestión de evaluaciones docentes que permita asignar pares aleatorios para coevaluación, verificar la coherencia entre diferentes evaluadores, calcular promedios y mostrar un cronograma de entregas, todo a través de un menú interactivo que se repita hasta que el usuario decida salir.

Al construirlo, aprendimos a organizar código en **3 capas** (Datos, Funciones, Interfaz), implementar **clases en Python** y utilizar estructuras como `random.shuffle()` y `while True` para crear un sistema interactivo y funcional.


## Cómo ejecutar el código

```bash
# Clonar el repositorio
git clone https://github.com/tu-organizacion/tumbaco-sheyla-unidad3.git

# Entrar a la carpeta del proyecto
cd tumbaco-sheyla-unidad3

# Ejecutar el programa
cd src
python main.py


---

``
``## Estructura del repositorio 
tumbaco-sheyla-unidad3/
├── src/
│ ├── main.py                     # Menú principal (Capa 3 - Interfaz)
│ ├── estudiantes.py              # Datos de estudiantes (Capa 1 - Datos)
│ ├── evaluaciones.py             # Datos de evaluaciones (Capa 1 - Datos)
│ ├── gestion_evaluaciones.py     # Lógica de negocio (Capa 2 - Funciones)
│ ├── test_funciones.py           # Pruebas unitarias
│ ├── database.py                 # Conexión a base de datos
│ ├── taller8-automatizacion      # Taller de automatización
│ ├── .gitignore                  # Archivos ignorados en GitHub
│ ├── BITACORA.md                 # Registro de avances por fase
│ └── README.md                   # Este archivo
└── docs/
    └──  (documentación, capturas, diagramas)
```

--- 

## Decisiones de diseño

``
Organización en 3 capas

Separar el código en 3 capas nos ayuda a mantener el código ordenado y facilitar la depuración:

Capa Archivo Descripción
Capa 1: Datos estudiantes.py, evaluaciones.py Lista de estudiantes y diccionario de evaluaciones
Capa 2: Funciones gestion_evaluaciones.py 
Capa 3: Interfaz main.py Menú interactivo con while True

Estructuras adicionales

· import random: Para generar parejas aleatorias con random.shuffle().
· while True: Permite que el menú se repita hasta que el usuario decida salir.
· match case: Maneja las opciones del menú de forma clara y legible.
``

## Problemas encontrados y cómo los resolviste

Error 1: Malinterpretación del alcance del proyecto

Problema: Pensamos que el proyecto era sobre gestión de estudiantes con correo e identificación.
Solución: Revisamos la rúbrica varias veces y nos dimos cuenta de que el tema era "Automatización de Logística y Coherencia" enfocado en evaluación docente.
Lección: Leer las instrucciones al menos 3 veces antes de empezar a codificar.

Error 2: Uso de import random y while True

Problema: No habíamos visto estas estructuras en clase.
Solución: Investigamos por nuestra cuenta en la documentación oficial de Python y en tutoriales. Implementamos random.shuffle() para mezclar estudiantes y while True para el bucle del menú.

Error 3: Organización en capas

Problema: Dificultad para separar el código en capas.
Solución: Usamos archivos separados: estudiantes.py, evaluaciones.py, gestion_evaluaciones.py y main.py.

Error 4: Strings en Python

Problema: Usamos "Un" + " " + 45 en lugar de "=" * 45.
Solución: Aprendimos que en Python no se puede sumar un string con un número; hay que usar multiplicación de strings ("texto" * N).

Error 5: Importación incorrecta

Problema: Usamos from src.services.gestion_evaluation import GestionEvaluacion (inglés).
Solución: Corregimos a from src.services.gestion_evaluacion import GestionEvaluacion (español).


---

# [Taller Asignación estudiantes]


# Modulo: Este taller implementa una asignación de parejas para su respectiva evaluacion y coevaluacion durante el proyecto en grupo
# Elementos:
# id_evaluacion:
Identificador único de la evaluación
## fecha: Fecha de evaluación
# profesor1: 
Nombre del primer profesor
# profesor2: 
Nombre del segundo profesor
# estado_coherencia:
Estado de coherencia (por defecto "No")
# Métodos:
__init__(id_evaluacion, fecha, profesor1, profesor2): Constructor de clase 

# REFLEXIÓN FINAL 
¿Qué haríamos diferente?

· Leer la rúbrica con más atención desde el principio para evitar malentendidos.
· Planificar mejor las capas antes de empezar a codificar.
· Hacer commits más pequeños en GitHub para tener un mejor historial de cambios.

¿Qué fue lo más difícil?

· Entender cómo organizar el código en capas.
· Implementar random.shuffle() correctamente para que las parejas cambien cada vez.
· Depurar errores de sintaxis como los strings mal escritos.

Conclusión

Este proyecto nos enseñó que la programación no es solo escribir código, sino también planificar, organizar y trabajar en equipo. Aprendimos a usar GitHub para colaborar, a documentar nuestro proceso y a resolver problemas de forma autónoma. ¡Fue una experiencia enriquecedora!

---

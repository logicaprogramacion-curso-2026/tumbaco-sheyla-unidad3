# [AUTOMATIZACIÓN DE LOGÍSTICA Y COHERENCIA]
**Alumno:** [Tumbaco, Sheyla]
# [NTEGRANTES DEL PROYECTO]
---
**DOMENICA BELEN RODRIGUEZ NARANJO**
**MAYDELEINE SAMIRA SANCHEZ MONROY**
**SHEYLA ARLETTE TUMBACO MORÁN**

**Curso:** [Lógica de Programación]
**Fecha de inicio:** [12/06/2026]
--- 

## 1. Objetivo del proyecto

Desarrollar un sistema automatizado para la gestión de evaluaciones docentes que permita asignar pares aleatorios para coevaluación, verificar la coherencia entre diferentes evaluadores, calcular promedios y mostrar un cronograma de entregas, todo a través de un menú interactivo que se repita hasta que el usuario decida salir.

Al construirlo, aprendimos a organizar código en **3 capas** (Datos, Funciones, Interfaz), implementar **clases en Python** y utilizar estructuras como `random.shuffle()` y `while True` para crear un sistema interactivo y funcional.


## 2. Cómo ejecutar el código

```bash
# Clonar el repositorio
git clone https://github.com/tu-organizacion/tumbaco-sheyla-unidad3.git

# Entrar a la carpeta del proyecto
cd tumbaco-sheyla-unidad3

# Ejecutar el programa
cd src
python main.py


## 3. Estructura del repositorio


```
tumbaco-sheyla-unidad3/
├── src/
│ ├── main.py # Menú principal (Capa 3 - Interfaz)
│ ├── estudiantes.py # Datos de estudiantes (Capa 1 - Datos)
│ ├── evaluaciones.py # Datos de evaluaciones (Capa 1 - Datos)
│ ├── gestion_evaluaciones.py # Lógica de negocio (Capa 2 - Funciones)
│ ├── test_funciones.py # Pruebas unitarias
│ ├── database.py # Conexión a base de datos
│ ├── taller8-automatizacion # Taller de automatización
│ ├── .gitignore # Archivos ignorados en GitHub
│ ├── BITACORA.md # Registro de avances por fase
│ └── README.md # Este archivo
└── docs/
    └── (documentación, capturas, diagramas)
```
--- 

## 4. Decisiones de diseño

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


## 5. Problemas encontrados y cómo los resolviste

Semana 1 - Estructura base (12/06/26)

Hoy nos reunimos y organizamos nuestro proyecto de la siguiente manera:

· Decidimos hablar primero acerca sobre lo que haremos de proyecto, que en nuestro caso será sobre una automatización de gestión de procesos.
· Realizamos las estructuras de carpetas en una hoja de cuaderno para poder guiarnos.
· Todas estas carpetas serán llevadas a GITHUB para que nuestro docente pueda visualizar nuestras carpetas, códigos y documentos.
· Nos repartimos cada una que parte haremos para nuestro proyecto:
  · Capa 1 (DATOS): SHEYLA TUMBACO
  · Capa 2 (FUNCIONES): DOMENICA RODRIGUEZ
  · Capa 3 (MENÚ): SAMIRA SANCHEZ

Estructuras adicionales implementadas:

· import random: Para que las parejas de estudiantes sea al azar.
· while True: Permite que nuestro menú se repita varias veces.

---


Semana 2 - Elaboración de Definiciones del Proyecto (15/06/26)

Esta semana nos enfocamos en crear nuestros Objetivos generales, específicos y los requerimientos de nuestro proyecto.

Objetivo general: Desarrollar un sistema para gestionar procesos logísticos y de coherencia, optimizando el flujo de trabajo y mejorando la coordinación entre los participantes.

Objetivos específicos:

· Registrar estudiantes con nombre, correo e identificación
· Consultar, buscar, actualizar y eliminar estudiantes
· Generar parejas o grupos de manera aleatoria
· Reorganizar grupos automáticamente
· Registrar fechas importantes
· Gestionar tareas y actividades asignadas a grupos
· Consultar historial de asignaciones
· Comparar resultados entre actividades
· Calcular estadísticas básicas
· Menú interactivo con while True
· Validar datos ingresados
· Generar reportes

Lección aprendida: Nos dimos cuenta de que habíamos malinterpretado la tarea al principio. Pensamos que el proyecto era sobre registrar estudiantes con correo, identificación y gestionar actividades, pero después nos dimos cuenta de que el proyecto era sobre un sistema de comparación de notas entre evaluadores y asignación de parejas.

---


Semana 3 - Prototipo de Capa 1 y 2 (19/06 - 22/06/26)

Entre estas fechas nos dedicamos a agregar la capa 1 y 2 en nuestro código de automatización.

CAPA 1 (DATOS): Se utilizó lista para agregar los nombres de cada estudiante (5 estudiantes) y un diccionario para las calificaciones: nota_profesor1, nota_profesor2, autoevaluacion.

CAPA 2 (FUNCIONES): Utilizamos def para crear nuestras funciones:

· asignar_pares(lista): Asigna pares de estudiantes aleatoriamente.
· mostrar_fechas(): Muestra las fechas de entrega.
· calcular_diferencia(n1, n2, n3): Calcula la diferencia porcentual entre la nota más alta y más baja.
· estan_de_acuerdo(n1, n2, n3): Determina si los evaluadores están de acuerdo (diferencia <= 20%).
· calcular_nota_final(n1, n2, n3): Calcula la nota final con ponderación (40% cada profesor, 20% autoevaluación).

---


Semana 4 - Pruebas y Estructura Final (Actual)

· Implementación de pruebas unitarias en test_funciones.py
· Creación de database.py para conexión a base de datos
· Organización final del repositorio
· Documentación completa en README.md y BITACORA.md

---


## 6. Reflexión final


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


# Taller Asignación estudiantes

##Modulo: Este taller implementa una asignación de parejas para su respectiva evaluacion y coevaluacion durante el proyecto en grupo
## Elementos:
id_evaluacion: Identificador único de la evaluación
fecha: Fecha de evaluación
profesor1: Nombre del primer profesor
profesor2: Nombre del segundo profesor
estado_coherencia:Estado de coherencia (por defecto "No")
## Métodos:
__init__(id_evaluacion, fecha, profesor1, profesor2): Constructor de clase 

---
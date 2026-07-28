# [AUTOMATIZACIÓN DE LOGÍSTICA Y COHERENCIA]

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
**Fecha de inicio:** [27/07/2026]
--- 


## DESCRIPCION

Sistema que carga preguntas desde archivos TXT, CSV y JSON, las almacena en SQLite, simula evaluaciones y genera reportes.

---

## ESTRUCTURA DEL PROYECTO


```
taller9-banco_preguntas/
├── preguntas.txt
├── preguntas.csv
├── preguntas.json
├── src/
│ ├── entidad.py
│ ├── dao.py
│ ├── gestor.py
│ ├── simulador.py
│ └── main.py
├── database/
├── resultados/
├── tests/
├── requirements.txt
└── README.md

---

## REQUISITOS
- Python 3.8+
- SQLite3

---

## COMO EJECUTAR

cd taller9-banco_preguntas
python src/main.py

MENU PRINCIPAL

1 -> Cargar preguntas desde archivo
2 -> Ver todas las preguntas
3 -> Ver estadisticas
4 -> Iniciar simulacion
5 -> Exportar datos
6 -> Ver reportes
7 -> Salir

---
## Iteracion 1: Configuracion Inicial

Se creo la estructura de carpetas y archivos base del proyecto.
Se implemento la clase Pregunta con sus atributos y metodos.
Se creo el archivo README.md con la descripcion del proyecto.

## Iteracion 2: Creacion de Archivos

Se generaron los archivos preguntas.txt, preguntas.csv y preguntas.json.
Cada archivo contiene 50 preguntas de programacion en Python.
Se verifico que todos los archivos tengan las mismas preguntas.
 ## Iteracion 3: DAO y Base de Datos

Se implemento la clase PreguntaDAO con conexion a SQLite.
Se creo la tabla preguntas con todos los campos requeridos.
Se implementaron los metodos CRUD basicos.

Iteracion 4: Carga de Datos desde Archivos

Se implementaron los metodos de carga desde TXT, CSV y JSON.
Se convirtieron los datos a objetos Pregunta.
Se validaron los campos obligatorios.

Iteracion 5: Guardado en Base de Datos y Exportacion

Se implemento el guardado en base de datos.
Se crearon los metodos de exportacion a TXT, CSV y JSON.

Iteracion 6: Implementacion del Simulador

Se creo la clase Simulador con seleccion aleatoria de preguntas.
Se implemento la presentacion interactiva y validacion de respuestas.
Se calcula el puntaje automaticamente.

Iteracion 7: Generacion de Reportes

Se implementaron reportes en TXT, CSV y JSON.
Los reportes incluyen fecha, preguntas, respuestas y puntaje.

Iteracion 8: Integracion Final y Pruebas

Se crearon pruebas unitarias para entidad y DAO.
Se implemento el menu completo con todas las opciones.
Se verifico la integracion de todos los modulos.

---
 PRUEBAS REALIZADAS

Prueba de creacion de pregunta: OK
Prueba de conversion a diccionario: OK
Prueba de conexion a base de datos: OK
Prueba de insercion y recuperacion: OK
Prueba de conteo de preguntas: OK
Prueba de carga desde TXT: OK
Prueba de carga desde CSV: OK
Prueba de carga desde JSON: OK
Prueba de simulacion: OK

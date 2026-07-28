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
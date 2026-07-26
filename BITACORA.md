# Bitácora de avances

Registra aquí cada sesión de trabajo. Un commit por avance, con un mensaje claro (ver guía abajo).

## Cómo escribir buenos mensajes de commit

- ❌ `arreglos`, `cambios`, `avance`
- ✅ `Implementa función de búsqueda binaria en lista ordenada`
- ✅ `Corrige error de índice fuera de rango en recorrido de matriz`
- ✅ `Agrega validación de entrada en menú principal`

## Registro de sesiones

### [12/06/26] — Semana 2: Estructura base

- Qué hicimos:

Hoy nos reunimos y organizamos nuestro proyecto de la siguiente manera:
· Decidimos hablar primero acerca sobre lo que haremos de proyecto, que en nuestro caso será sobre una automatización de gestión de procesos.

· Realizamos las estructuras de carpetas en una hoja de cuaderno para poder guiarnos.
· Todas estas carpetas serán llevadas a GITHUB para que nuestro docente pueda visualizar nuestras carpetas, códigos y documentos.
· Nos repartimos cada una que parte haremos para nuestro proyecto:
  · Capa 1 (DATOS): SHEYLA TUMBACO
  · Capa 2 (FUNCIONES): DOMENICA RODRIGUEZ
  · Capa 3 (MENÚ): SAMIRA SANCHEZ

Así que nos pusimos a charlar y compartir nuestras ideas. Decidimos hacer todo esto de acuerdo a lo que nos han enseñado, tomando en cuenta algunos conceptos para poder darle vida a nuestro programa, así que investigamos más a fondo para que el programa sea más útil y completo.
Como haremos una automatización utilizaremos estas estructuras adicionales:

- import random: Nos pidieron que las parejas de estudiantes sea al azar. Para eso, decidimos usar import random y random.shuffle() que mezclará la lista de estudiantes. 
Sin esto, las parejas siempre serían las mismas, así que cada ves que el usuario elija la opción 1, saldrán parejas diferentes.

- while True: Nos va a permitir que nuestro menú se repita varias veces después de cada opción, permite que el bucle este activo. Sin este bucle si elegimos una opción ya no nos va a poder permitir seguir eligiendo más opciones y el programa acabaría en una sola opción.
Ayuda a que el usuario pueda hacer parejas, ver fechas, comparar notas y calcular el final, sin tener que abrir el programa cada vez.

Estas dos estructuras serán nuestro punto clave para poder realizar nuestra automatización de la mejor manera.

Hasta ahora es todo lo que tenemos para esta semana, vamos a hacer pruebas para nuesto programa, ver las posibles soluciones y fallas y ayudándonos mutuamente si se nos complica entender algo, aunque las dos partes de las estructuras será un reto para nosotras, haremos lo posible para que nuestro programa funcione completamente.

- Qué problemas encontramos:

Utilizar los dos códigos necesarios para la automatización, ya que es nuestra primera vez utilizando estos códigos, fue algo complejo pero hicimos lo posible para implementarlo de la mejor manera.

- Cómo lo resolvimos:

Investigamos más a fondo sobre estas líneas de código y como utilizarlas en este programa.

- Próximo paso:

Creación de Objetivos generales y objetivos específicos.

### [15/06/26] — Semana 3: [Elaboración de Definiciones del Proyecto]

- Qué hicimos:

Esta semana nos enfocamos en crear nuestros Objetivos generales, específicos y los requerimientos de nuestro proyecto. Esta fue una tarea asignada por nuestro docente y se realizó de manera individual. 
Cada una describió cada punto requerido para el proyecto en base a nuestro diagrama.
Esta fue una de las formas en la que se describió los puntos:

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
· Actualizar información sin reiniciar
· Registrar fecha y hora automáticamente

Requerimientos funcionales (30 en total):

· Gestión de estudiantes: registrar, consultar, buscar, actualizar, eliminar
· Gestión de grupos: generar parejas, crear grupos, evitar duplicados, consultar, reorganizar
· Gestión de actividades: registrar, asignar a grupos, consultar pendientes, marcar completadas, registrar observaciones
· Gestión de fechas: registrar, consultar próximas, validar, mostrar por fecha, registrar automáticamente
· Menú y validación: while True, múltiples operaciones, validar opciones, try/except
· Reportes: generar reportes, historial, comparar resultados, estadísticas, resumen general


- Qué problemas encontramos:

Nos dimos cuenta de que habíamos malinterpretado la tarea al principio. Pensamos que el proyecto era sobre registrar estudiantes con correo, identificación y gestionar actividades, pero después nos dimos cuenta de que el proyecto era sobre un sistema de comparación de notas entre evaluadores y asignación de parejas.
Así que volvimos a redactar bien nuestros objetivos.

**OBJETIVO PRINCIPAL**

Crear un sistema automatizado para la gestión de evaluaciones docentes que permita:

· Asignar pares aleatorios para coevaluación
· Verificar la coherencia entre diferentes evaluadores
· Calcular promedios
· Mostrar un cronograma de entregas. Todo a través de un menú interactivo que se repita hasta que el usuario decida salir

---

**OBJETIVOS ESPECÍFICOS**

1. Gestión de Datos Básicos

· Mantener un catálogo de estudiantes con sus nombres
· Administrar las notas de cada estudiante provenientes de 3 evaluadores (Profesor 1, Profesor 2 y Autoevaluación)
· Almacenar las fechas de entrega de las evaluaciones

---

2. Gestión de Evaluaciones

· Registrar 3 notas por estudiante (Profesor 1, Profesor 2 y Autoevaluación)
· Comparar las notas de los diferentes evaluadores para detectar discrepancias
· Calcular automáticamente la diferencia emn porcentaje entre la nota más alta y la más baja
· Establecer el 20% para determinar si los evaluadores están de acuerdo
· Calcular la nota final: 40% Profesor 1, 40% Profesor 2, 20% Autoevaluación

---

3. Gestión de Coherencia

· Detectar automáticamente si los evaluadores están de acuerdo
· Identificar desaacuerdos mayores al 20% entre evaluadores
· Mostrar mensajes claros sobre el estado de la coherencia

---

4. Gestión de Coevaluación

· Asignar aleatoriamente pares de estudiantes para coevaluación
· Mostrar las parejas asignadas claramente
· Asegurar que ningún estudiante quede sin par (mostrar "Sin par" cuando corresponda)

---

5. Gestión de Tiempos

· Mostrar un cronograma claro de las fechas de entrega
· Presentar las fechas de forma ordenada y visual

---

6. Interfaz de Usuario

· Proporcionar un menú interactivo con opciones claras
· Mantener el menú activo hasta que el usuario decida salir
· Validar las opciones ingresadas por el usuario
· Mostrar mensajes de error para opciones inválidas

---

7. Arquitectura del Sistema

· Organizar el código en 3 capas:
  · Capa 1: Datos (estudiantes, evaluaciones)
  · Capa 2: Lógica (funciones de procesamiento)
  · Capa 3: Interfaz (menú interactivo)
· Mantener el código limpio y estructurado

---

- Cómo lo resolvimos:

Cuando nos dimos cuenta de que habíamos entendido mal la tarea, volvimos a leer bien las indicaciones del proyecto. Ahí entendimos que no era un sistema para registrar estudiantes, sino uno para comparar notas entre evaluadores y asignar parejas. Entonces cambiamos lo que ya habíamos hecho y empezamos a desarrollar las funciones que realmente pedía el proyecto, revisando que todo estuviera de acuerdo con los requisitos.

- Próximo paso:

Realización de prototipo por capas

## [19/06 - 22/06] — Semana 4: [Prototipo de Capa 1 y 2 sin LLM. Código que carga datos y ejecuta la lógica central (versión mosk)]

- Qué hicimos:
Entre estás fechas nos dedicamos a agregar la capa 1 y 2 en nuestro código de automatización, luego de corregir nuestro error empezamos desde 0.
CAPA 1: Se muestran los datos, se utilizó lista para agregar los nombres de cada estudiante, elegimos 5 estudiantes.
También agregamos un diccionario para poner las calificaciones que se requieren de acuerdo a las indicaciones de nuestro proyecto, que son nota_profesor1, nota_profesor2, autoevaluacion.

CAPA 2: Utilizamos def para crear nuestras funciones, creamos la línea de código def asignar_pares():
Esto significa que la función recibe una lista de estudiantes como variables, en donde debajo se colocará:
pares = [] 
Que servirá para almacenar los pares de estudiantes.

Debajo de esta sigue cantidaad = len(lista), nos ayudará a obtener la cantidad de estudiantes en nuestra lista.
Procedemos con la función for i in range, esta función va ayudarnos a recorrer nuestra lista de estudiantes en dos en dos, de manera par.
Entonces quedaría for i in range(0, cantidad, 2):
0 es solo porque el rango inicia en 0, termina en la cantidad de estudiantes y se incrementa de 2 en 2.

if i + 1 < cantidad:
            pares.append((lista[i], lista[i + 1]))
        else:
            pares.append((lista[i], "Sin par"))
Nos pregunta si existe un estudiante en la posición i + 1, i es la posición que va cambiando, i puede ser 1,2,3.. 
Nos dice; Si i + 1 es.. significa la posición de al lado de por ejemplo Ana es Luis.
Entonces agregamos pares.append, que nos agregará la pareja de la lista de pares, esta en nuestro código para guardar la pareja completa y el .append es el que agrega un elemento final de la lista.
¿Por qué el sin par?
Esta para que la persona no quede olvidada, nos indica que si no hay un compañero que asigne que es "Sin par", por eso usamos else, Si no.. es "Sin par".
Entonces haremos que nos devuelva la lista utilizando:
return pares
Para que el menú pueda mostrar el resultado.

Ahora mostraremos las fechas de entragas y del proyecto
def mostrar_fechas():
    print(" * Tarea 1: 20/06/2026")
    print(" * Tarea 2: 27/06/2026")
    print(" * Proyecto: 10/07/2026")

Vamos a calcular la diferncia en porcentaje entre la nota más baja y alta, utilizando primero la función de:
def calcular_diferencia(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        mayor = n1
    elif n2 >= n1 and n2 >= n3:
        mayor = n2
    else:
        mayor = n3
Nos pregunta si nota1 es la más alta entre las tres y mayor = n1 nos dice que si la condición es veerdadera entonces nota 1 si es la nota más alta.
Si no puede ser que nota2 es mayor entre las tres y si la función se cumple como verdadera, entonces nota2 si es la más alta.
else sería si no, entonces la nota mayor es nota3.

Ahora sacaremos la nota más baja, el procedimiento es el mismo solo que en vez de ser mayor es menor.
if n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    else:
        menor = n3
Sacaremos la diferncia etre las notas, para esto utilizamos la siguiente función:
diferencia = ((mayor - menor) * 100) // mayor
    return diferencia
En esta línea de códgo utlizamos (( para que en nuestro programa se pueda agrupar las operaciones y ya sea en Python o Collab para que en estos programas se le indique que haceer primero.
El paréntesis interno realiza la operación, mientras que en la externa va a multiplicarlo por 100 para sacar la diferencia entre las notas.
Sin estos paréntesis tendríamos resultados incorrectos, por qué si no primero realizaría la multiplicación y no es lo que buscamos, por lo que hay que seguir la estructura de Python, ya que sin esta no podríamos realizar la operación a como se indica. No es lo mismo realizar operaciones como usualmente las hacemos que en programación, donde es más estricto las órdenes para realizar operaciones.
Entones su orden quedaría que establece una variable y que realice una operación, primero realiza lo de dentro y luego lo de afuera, así obtenemos nuestro resultado de diferencia.
Entonces devolveremos el número de diferencia, para que el estan_de-acuerdo se pueda utilizar.
return diferencia

Ponemos nuestra función def estan_de_acuerdo(n1, n2, n3):
Para oder ver si los resultados son coherentes, entonces calculamos su diferencia y decimos que:
diferencia = calcular_diferencia(n1, n2, n3)
Nos dice que si calcular_diferncia entre las tres notas 
if diferencia <= 20:
        return "Están de acuerdo"
    else:
        return "No están de acuerdo"
Si la diferencia es menor que 20 que devuelva que estan de acuerdo, si no que simplemente no.

Vamos a calcular las notas finales de acuerdo a los asignado en nusestro oroyecto, que los profesores cuentan con un 40% cada uno y la evaluación es de 20%.
def calcular_nota_final(n1, n2, n3):

Entonces decimos que si la nota es igual a nota1 por 40 más nota2 por 40 más nota3 por 20 que esto se divida entre 100.

    nota = (n1 * 40 + n2 * 40 + n3 * 20) // 100
    return nota
Ahora devolvemos la nota final para poder ser visualizada en el menú.

MENÚ
En nuestro menú implementamos:
print("\n" + "=" * 45)
print("SISTEMA DE COORDINACIÓN DOCENTE")
print("=" * 45)
print(" Grupo 7 - Lógica de Programación")
print("=" * 45)
Esto es solo para que se imprima nuestro título de manera más organizada.

Ahora utilizamos el while true para que se pueda generar un bucle al momento de que este todo listo poder elegir ente varias opciones sin generar errores.
while True:
    print("\n" + "-" * 35)
    print(" 1 → Hacer parejas al azar")
    print(" 2 → Ver fechas de entrega")
    print(" 3 → Ver si los profesores están de acuerdo")
    print(" 4 → Calcular nota final del estudiante")
    print(" 5 → Salir")
    print("-" * 35)
Para que se pueda cumplir el que genere varias opciones, asignaremos que el usuario tenga el acceso a esta opción.
opcion = input(" ➤ Elige: ")
input sirve para que el usuario pueda guardar el dato en la variable.

Ahora para ejecutar las opciónes elegidas por el usuario utlizaremos match case, que agregaremos lo que le corresponde al menú.

match opcion:
        case "1":
            print("\n HACIENDO PAREJAS...")
            copia = estudiantes.copy()
            random.shuffle(copia)
            pares = asignar_pares(copia)
            print("\n PAREJAS:")
            for p in pares:
                print(f" {p[0]} ↔ {p[1]}")
La copia = estudiantes.copy() Creará una copia de la lista de estudiantes para no modificar la  original.
random.shuffle(copia) Mezclará nuestra lista al azar.
pares = asignar_pares(copia) Llamará a laa función para hacer parejas.
for p in pares Nos indicará que va a recorrer cada pareja y la va a imprimir por eso el print (f" {p[0]} ↔ {p[1]}") f par meter variabes dentro del texto y {p[0]} para el primer elemento de pareja y el {p[1]} el segundo elemento de pareja.
El simbolo de las flechas de un lado a otro es un simbolo que interpreta "con".

Esta parte solo imprime las fechas de entrega y la mostrará.
case "2":
            print("\n FECHAS DE ENTREGA:")
            mostrar_fechas()

En el case 3 imprimirá la verificación  y el 20% de diferencia para estar de acuerdo.
case "3":
            print("\n VERIFICANDO...")
            print(" (Máx 20% de diferencia para estar de acuerdo)")
            print(" " + "-" * 35)
el print(" " + "-" * 35) sirve para separar visualmente las secciones del menú y 35 por que es el número de veces que se repite el símbolo, imprime 35 guiones seguidos, es solo para hacer una línea de separación más larga, para que nuestro mennú sea organizado.

Entonces vamos a recorrer el nombre y resultados de los estudiantes, declarando que:
for nombre in estudiantes:
                notas = evaluaciones[nombre]
                resultado = estan_de_acuerdo(notas[0], notas[1], notas[2])
                print(f" {nombre}: {notas[0]}/{notas[1]}/{notas[2]} → {resultado}")
Esto hará que al momento de mostar la opción asignada se pueda visalizar su nombre, las tres notas y su resultado.

El case 4 imprimiremos la nota final y que cada profesor tenga el 40% de la notas y las autoevaluaciones sean de 20% 
case "4":
            print("\n NOTA FINAL:")
            print(" (Cada profesor 40% | Autoevaluación 20%)")
            print(" " + "-" * 30)
Aquí el 30 es igual al que el 35, solo son líneas para organizar 
La nota final se calcula con 40% para cada profesor y el 20% de autoevaluación, quiere decir que los profesores tienen más peso porque su evaluación es más profesional y la autoevaluación tiene menos peso porque el estudiante puede evaluarse a sí mismo.

Ahora vamos a recorrer cada estudiante y que obtendrán sus tres notas, calcularemos su promedio y mostraremos el resultado
for nombre in estudiantes:
                notas = evaluaciones[nombre]
                nota_final = calcular_nota_final(notas[0], notas[1], notas[2])
                print(f" {nombre}: {nota_final} puntos")
Imprimiremos una despedida
case "5":
            print("\n ¡Hasta luego!")
            break
el break se utiliza para salir del bucle

Como pasos finales agregamos un mensaje de error para opciones inválidas.
case _:
            print(" Opción no válida. Elige 1,2,3,4 o 5.")

- Próximo paso:
Realización de Definicion de Estructuras del Proyecto

### [1/07/26] - Semana 5: [Definicion de Estructuras del Proyecto]

- Qué hicimos:

Definimos las clases "OpcionMenu" y "Evaluacion" para el proyecto.

# GRUPO 7
class OpcionMenu:
  id_opcion = ""
  nombre_opcion = ""
  descripcion = ""
  funcion_asociada = ""
  requiere_datos = ""
  estado = ""
def __init__(self, id_opcion, nombre_opcion, funcion_asociada):
  self id_opcion = id_opcion
  self nombre_opcion = nombre_opcion
  self funcion_asociada = funcion_asociada


class evaluacion:
    id_evaluacion = ""
    fecha = ""
    profesor1 = ""
    profesor2 = ""
    estado_coherencia = "No"

    def __init__(self, id_evaluacion, fecha, profesor1, profesor2):
        self.id_evaluacion = id_evaluacion
        self.fecha = fecha
        self.profesor1 = profesor1
        self.profesor2 = profesor2

- Qué problemas encontramos:

Ninguno.

- Próximo paso:

Selección de Sistemas de Gestión Docente

## [7/07/26] - Semana 6: [Selección de Sistemas de Gestión Docente]

- Qué hicimos:
El profesor revisó la simulación de tarea.
Verificó que el sistema funciona correctamente.

- Qué problemas encontramos:

Nos indicó que no ejecutaba correctamente y que hubo una falla. Volvió a intentarlo y funcionó.

### Observaciones del profesor:

- El sistema funciona correctamente.
- Se detecta correctamente cuando hay desacuerdo (David).
- Las notas finales se calculan con la ponderación adecuada.

- Próximo paso:

Continuar con el desarrollo según indicaciones del profesor.

## [14/07/26] Taller 7: [Practica sobre manejo de repositorio digital]

- Qué hicimos:

Hicimoms un taller de manera individual en la que realizamos una práctica sobre el manejo de repositorio digital. 
Realizamos esta practica de acuerdo al instructivo que nos asignaron para este taller.
1. Entré al enlace que dio el profesor https://github.com/logicaprogramacion-curso-2026/plantilla-proyecto-logica-programacion
2. Hice clic en "Use this template" y luego en "Create a new repository".
3. Cambié el Owner a logicaprogramacion-curso-2026 para que el repositorio quedara en la organización del curso y no en mi cuenta personal.
4. Le puse el nombre con el formato apellido-nombre-unidad3, todo en minúsculas y con guiones.
5. Verifiqué que el repositorio fuera visible para la organización.
6. Finalmente, hice clic en "Create repository".

**Paso 2: Clonar el repositorio**

Copié la URL de mi repositorio y la cloné en mi computadora usando Git. Después entré a la carpeta del proyecto para comenzar a trabajar.

**Paso 3: Organizar las tareas**

Cada vez que había una nueva tarea o taller, creé una carpeta con su nombre correspondiente. Dentro de cada carpeta agregué un README.md y el código del proyecto para mantener todo organizado.

**Paso 4: Guardar el progreso**

Durante el desarrollo fui haciendo commits con mensajes claros que indicaban qué cambio había realizado en cada tarea. También subí los cambios a GitHub de forma constante, en lugar de hacerlo todo al final, para que quedara registrado mi progreso.

- Próximo paso: Realización de taller 8

## [21/07/26] Taller 8: [Repositorio inicial del proyecto]

TALLER 8 - AUTOMATIZACIÓN DE LOGÍSTICA Y COHERENCIA

**Grupo 7 - Lógica de Programación**

---

## PROPÓSITO

El propósito de este taller es trabajar en el repositorio inicial del proyecto, elaborando el directorio `taller8-automatizacion` y el archivo `README.md` con la documentación completa del sistema de automatización de logística y coherencia.

---

## INTEGRANTES

- DOMENICA BELEN RODRIGUEZ NARANJO
- MAYDELEINE SAMIRA SANCHEZ MONROY
- SHEYLA ARLETTE TUMBACO MORÁN


---



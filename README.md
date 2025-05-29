# ProyectoArboles
## Universidad Industrial de Santander
**Materia:** Estructura de Datos y análisis de algoritmos
**Fecha de entrega:** 29/05/2025

# Integrantes:
- Kevin David Basto Quintero 2222974
- Andres Santiago Culman Sanchez 2241929

# Contexto del problema
El pyoyecto consiste en modelar el recorrido de un camión de valores por diferentes direcciones(bancos, cajeros). En la primera entrega, se utilizó una lista doblemente enlazada para representar las rutas. En la segunda entrega, se optimizó el sistema usando árboles, lo cual permitió una estructura más jerárquica y eficiente para representar y gestionar las rutas a partir de la posición inicial del camión como nodo raíz. Para esta tercera entrega se modela y optimiza el recorrido de un camión de valores que transporta dinero a distintos destinos. A diferencia de las entregas anteriores, en esta etapa se implementa un **grafo dirigido ponderado** que permirte representar rutas más flexibles y realistas entre puntos, tomando en cuenta:
- Las prioridades de los destinos (Banco>Cajero)
- La distancia entre ellos (pesos en las aristas)
- Condiciones externas como clima o tráfico
- Visualización del mapa de rutas

## Evolución del proyecto

## Primera entrega - Lista doblemente enlazada
Se usó una estructura lineal donde cada dirección se insertaba secuencialmente. Se implementaron funciones básicas como insertar, eliminar, contar y buscar.
## Segunda entrega - Árbol no binario con bigtree
Se implementó un arbol con la raíz como punto de partida (posición del camión). Se mejoró la organización jerárquica y se introdujo la agrupación por niveles de distancia
## Tercera entrega - Grafo dirigido ponderado
En esta fase, se diseñó un sistema completo basado en grafos para representar todas las posibles rutas entre nodos. Cada nodo representa un destino (banco o cajero) y cada arista representa una conexión entre ellos con un peso asociado (distancia o tiempo).

## Funciones implementadas

### Funciones del grafo
- **encontrarCaminos()** - Encuentra todos los caminos posibles entre dos nodos
- **filtrarCaminos()** - Retorna solo caminos que cumplen con cierta prioridad (ej. Solo bancos)
- **findShortestPath()** - Determina el camino más corto entre 2 nodos (sin prioridad)
- **BFS()/ DFS()** - Recorridos en anchura y profundidad del grafo
- **pesoCamino()** - Calcula el peso total de un camino
- **ordenarCaminos()** - Ordena los caminos según el peso total

### Funciones auxiliares
- **crearPrioridad(), setPrioridad(), buscarPrioridad()** - Gestionan y asignan prioridad por tipo de destino
-  **calcularExito()** - Simula si el camión completa la ruta según el clima (aleatorio si hay mal clima)
- **visualizarGrafo()** - Visualiza el grafo completo

## Ejemplo de funcionamiento

1. El usuario ingresa los nodos (ej: 1, 2, 3) y sus tipos (Banco o Cajero).
2. Luego se definen las conexiones (aristas) entre nodos y sus pesos.
3. El sistema construye un grafo dirigido y ponderado.
4. Se pregunta si hay inclemencias climáticas y se simula si la ruta fue completada o fallida.
5. El grafo se visualiza como un mapa de rutas dirigido.

## Conclusión
Comparado con las entregas anteriores (listas doblemente enlazadas y árboles), el grafo ponderado es mucho más eficiente y permite una representación más flexible de las rutas, lo cual permite simular rutas más realistas y eficientes. Permitiendo una planificación más dinámica, control por prioridad, análisis de eficiencia, y adaptabilidad ante factores externos.
Este modelo permite:
- Representar rutas no jerarquicas, donde un mismo nodo puede ser alcanzado desde múltiples caminos
- Incorporar pesos realistas
- Aplicar prioridades (como Banca>Cajero)
- Simular situaciones reales como el clima adverso
- Visualizar la red de rutas de forma clara e interactiva
### Tecnologías usadas
- Python 3.10+
- igraph
- matplotlib
- random
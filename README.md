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



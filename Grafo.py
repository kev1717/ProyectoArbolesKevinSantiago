import igraph as ig
import random
from igraph import Graph, plot

# --------------------- Funciones auxiliares ----------------------

#Prioridad de cada nodo del grafo respecto a su tipología, devuelve un vector con prioridades
def setPrioridad(listNames):
    prioridades = []
    for i in range(len(listNames)):
        if listNames[i] == "Banco":
            prioridades.append(1)
        elif listNames[i] == "Cajero":
            prioridades.append(2)
    return prioridades


#Crea una prioridad de cada nodo del grafo respecto a su tipología, devuelve un vector con prioridades
def crearPrioridad(listNames, indexnode):
    if indexnode < len(listNames):
        if listNames[indexnode] == "Banco":
            return 1
        elif listNames[indexnode] == "Cajero":
            return 2
    return 0  # Si el índice está fuera de rango

#Busca la prioridad del nodo iterando en la lista de nombres con el indice como argumento dado
def buscarPrioridad(listNames, indexnodeFromNodes):
    if indexnodeFromNodes < len(listNames):
        if listNames[indexnodeFromNodes] == "Banco":
            return 1
        elif listNames[indexnodeFromNodes] == "Cajero":
            return 2
    return 0  # Si el índice está fuera de rango

def calcularExito(grafo, condiciones):
    if condiciones.upper() == "SI":
        exito = random.random() > 0.5
        if exito:
            print("✅ Ruta completada a pesar de las inclemencias del clima.")
        else:
            print("❌ La ruta no pudo completarse por mal clima.")
    else:
        print("✅ Ruta completada exitosamente. No hubo inconvenientes.")

def visualizarGrafo(Nodes, names, edges, weights):
    g = Graph(directed=True)
    g.add_vertices(len(Nodes))
    node_to_index = {node: i for i, node in enumerate(Nodes)}
    g.vs["label"] = names
    indexed_edges = [(node_to_index[u], node_to_index[v]) for u, v in edges]
    g.add_edges(indexed_edges)
    g.es["weight"] = weights
    plot(g, layout=g.layout("circle"), bbox=(600, 600), margin=40)

# ----------------------- Clase del Grafo -------------------------

class grafoPonderado:
    #Modificación del constructor de la clase grafo ponderado
    def __init__(self, graph={}):
        self.grafo = graph

#Metodos
    #Principal: encuentra todos los caminos entre dos nodos
    def encontrarCaminos(self, nodoInicial, nodoFinal, camino=None):
        if nodoInicial not in self.grafo or nodoFinal not in self.grafo:
            return []
        if camino is None:
            camino = []
        camino = camino + [nodoInicial]
        if nodoInicial == nodoFinal:
            return [camino]
        caminos = []
        for nodoSiguiente, _, _ in self.grafo[nodoInicial]:
            if nodoSiguiente not in camino:
                subcaminos = self.encontrarCaminos(nodoSiguiente, nodoFinal, camino)
                for subcamino in subcaminos:
                    caminos.append(subcamino)
        return caminos

    #Ordenar caminos por peso de menor a mayor
    def ordenarCaminos(self, caminos):
        return sorted(caminos, key=self.pesoCamino)

    #Encuentra el peso total de un camino
    def pesoCamino(self, camino):
        pesoTotal = 0
        for i in range(len(camino) - 1):
            nodoActual = camino[i]
            for nodoDestino, peso, _ in self.grafo[nodoActual]:
                if nodoDestino == camino[i + 1]:
                    pesoTotal += peso
        return pesoTotal

    #Getter del peso de un camino
    def getPesoCamino(self,camino):
        return self.pesoCamino(camino)

     #Encuentra el camino mas corto entre dos nodos
    def findShortestPath(self, nodoInicial, nodoFinal, matrizCaminos=None):
        if matrizCaminos is None:
            matrizCaminos = self.encontrarCaminos(nodoInicial, nodoFinal)
        if not matrizCaminos:
            return []
        return self.ordenarCaminos(matrizCaminos)[0]

    #Obtiene el indice de un nodo especifico desde la matriz de aristas
    def getInidiceNodo(self, listaAristas, nodo):
        indiceForPeso = 0
        for nodoInicial, nodoFinal in listaAristas:
            if nodoInicial == nodo or nodoFinal == nodo:
                indiceForPeso = listaAristas.index((nodoInicial, nodoFinal))
        return indiceForPeso    #Obtiene el peso de un nodo (requerido para "filtrarCaminos")


    #Obtiene el peso de un nodo a partir del indice y la lista de pesos
    def getPesoForNodo(self, indicePeso, listaPesos):
        if 0 <= indicePeso < len(listaPesos):
            for i in range(len(listaPesos)):
                if i == indicePeso:
                    #Retorna el peso del nodo en la lista de pesos
                    return listaPesos[indicePeso]
        return 0  # Valor por defecto si el índice está fuera de rango


    #Selecciona los caminos posibles entre nodos cuyos nodos solo tengan la prioridad seleccionada
    def filtrarCaminos(self, nodoInicial, nodoFinal, matrizCaminos, listNames, listNodes, prioridad):
        caminosFiltrados = []

          #Manejo de casos especiales
        if not matrizCaminos:
            return []
        #Iteracion de cada camino en la matriz
        for camino in matrizCaminos:
            subFiltrados = [camino[0]] # Iniciar con el primer nodo
            #Iteracion de cada nodo sobre el camino ("len(camino) - 1" garantiza la existencia de [i + 1])
            for i in range(len(camino) - 1):
                nodoActual = camino[i]
                nodoSiguiente = camino[i + 1]
                #Verificar si nodoActual está en el grafo
                if nodoActual not in self.grafo:
                    break
                #Iteracion sobre el diccionario
                for nodoDestino, _, _ in self.grafo[nodoActual]:
                    #Obtener el indice del nodo destino en la lista de nodos
                    indexDestino = listNodes.index(nodoDestino) if nodoDestino in listNodes else -1
                    #Verifica si el nodo destino es el nodo siguiente y si la prioridad coincide
                    if nodoDestino == nodoSiguiente and buscarPrioridad(listNames, indexDestino) == prioridad:
                        if nodoSiguiente not in subFiltrados:
                            subFiltrados.append(nodoSiguiente)
                        break
            #Solo agregar si el camino llega al destino
            if subFiltrados[-1] == nodoFinal:
                caminosFiltrados.append(subFiltrados)
        return caminosFiltrados

    def DFS(self, nodo):
        visitados = [nodo]
        pila = [nodo]
        while pila:
            nodoActual = pila.pop()
            if nodoActual not in visitados:
                visitados.append(nodoActual)
                for nodoSiguiente, _, _ in self.grafo[nodoActual]:
                    if nodoSiguiente not in visitados:
                        pila.append(nodoSiguiente)
        return visitados

    def BFS(self, nodo):
        visitados = []
        queue = [nodo]
        while queue:
            nodoActual = queue.pop(0)
            if nodoActual not in visitados:
                visitados.append(nodoActual)
                for nodoSiguiente, _, _ in self.grafo[nodoActual]:
                    if nodoSiguiente not in visitados and nodoSiguiente not in queue:
                        queue.append(nodoSiguiente)
        return visitados

# ---------------------- Entrada de datos ------------------------
#Uso de la clase grafo:

#Creacion de nodos y nombres para cada uno mediante entrada por pantalla
Nodes = []
names = []
while True:
    try:
        node = int(input("Ingrese el número del nodo (0 para terminar): "))
        if node == 0:
            break
        name = input(f"Ingrese el nombre del nodo {node} (Banco/Cajero): ")
        if name not in ["Banco", "Cajero"]:
            print("Nombre inválido. Use 'Banco' o 'Cajero'.")
            continue
        Nodes.append(node)
        names.append(name)
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

print(f"nodos: {Nodes}")
print(f"nombres: {names}")

edges = []
weights = []
while True:
    edge_input = input("Ingrese la arista como 'nodo1 nodo2' (0 para terminar): ")
    if edge_input.strip() == "0":
        break
    try:
        nodo1, nodo2 = map(int, edge_input.split())
        if nodo1 not in Nodes or nodo2 not in Nodes:
            print("Uno de los nodos no existe.")
            continue
        peso = int(input(f"Ingrese el peso de la arista ({nodo1}, {nodo2}): "))
        edges.append((nodo1, nodo2))
        weights.append(peso)
    except ValueError:
        print("Entrada inválida.")

# ---------------------- Creación del grafo ------------------------

grafoDirigido = {}
for i, (nodoInicial, nodoFinal) in enumerate(edges):
    peso = weights[i]
    prioridad = crearPrioridad(names, Nodes.index(nodoInicial))
    if nodoInicial not in grafoDirigido:
        grafoDirigido[nodoInicial] = []
    grafoDirigido[nodoInicial].append((nodoFinal, peso, prioridad))
for node in Nodes:
    if node not in grafoDirigido:
        grafoDirigido[node] = []

print(f"prioridades: {setPrioridad(names)}")
print("Grafo ponderado:", grafoDirigido)

# ---------------------- Simulación y visualización ------------------------

strFallas = input("¿Hay inclemencias del clima? (SI/NO): ")
calcularExito(grafoDirigido, strFallas)
visualizarGrafo(Nodes, names, edges, weights)

# Instanciar objeto de grafo
grafo = grafoPonderado(grafoDirigido)

import igraph as ig
import random
from igraph import Graph, plot

# --------------------- Funciones auxiliares ----------------------

def setPrioridad(listNames):
    return [1 if name == "Banco" else 2 if name == "Cajero" else 0 for name in listNames]

def crearPrioridad(listNames, indexnode):
    return 1 if listNames[indexnode] == "Banco" else 2 if listNames[indexnode] == "Cajero" else 0

def buscarPrioridad(listNames, indexnodeFromNodes):
    return crearPrioridad(listNames, indexnodeFromNodes)

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
    def __init__(self, graph={}):
        self.grafo = graph

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

    def ordenarCaminos(self, caminos):
        return sorted(caminos, key=self.pesoCamino)

    def pesoCamino(self, camino):
        pesoTotal = 0
        for i in range(len(camino) - 1):
            nodoActual = camino[i]
            for nodoDestino, peso, _ in self.grafo[nodoActual]:
                if nodoDestino == camino[i + 1]:
                    pesoTotal += peso
        return pesoTotal

    def findShortestPath(self, nodoInicial, nodoFinal, matrizCaminos=None):
        if matrizCaminos is None:
            matrizCaminos = self.encontrarCaminos(nodoInicial, nodoFinal)
        if not matrizCaminos:
            return []
        return self.ordenarCaminos(matrizCaminos)[0]

    def filtrarCaminos(self, nodoInicial, nodoFinal, matrizCaminos, listNames, listNodes, prioridad):
        caminosFiltrados = []
        if not matrizCaminos:
            return []
        for camino in matrizCaminos:
            subFiltrados = [camino[0]]
            for i in range(len(camino) - 1):
                nodoActual = camino[i]
                nodoSiguiente = camino[i + 1]
                if nodoActual not in self.grafo:
                    break
                for nodoDestino, _, _ in self.grafo[nodoActual]:
                    indexDestino = listNodes.index(nodoDestino) if nodoDestino in listNodes else -1
                    if nodoDestino == nodoSiguiente and buscarPrioridad(listNames, indexDestino) == prioridad:
                        if nodoSiguiente not in subFiltrados:
                            subFiltrados.append(nodoSiguiente)
                        break
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

    # ===========================================
    # By: Nury Farelo - Estructuras Datos
    # Name: Taller 1 - Árboles - Parejas
    # ===========================================
    #Fecha 15/04/2025
    #Estudiantes:
    #Kevin David Basto Quintero 2222974
    #Andres Santiago Culman Sanchez 2241929

import bigtree
from bigtree import Node, print_tree

    #Raíz del arbol
posicionCamion = Node("raiz", distancia = 0, string = "Calle 32 #28-46")

    #Nodos hijos
direccion1 = Node("banco1", distancia = 2, string = "Calle 33 #29-68", parent = posicionCamion)
direccion2 = Node("banco2", distancia = 3, string = "Carrera 25 #32-72", parent = posicionCamion)
direccion3 = Node("cajeros1", distancia = 2, string = "Carrera 31 #32-31", parent = posicionCamion)
direccion4 = Node("cajeros2", distancia = 5, string = "Carrera 27 #28-83", parent = posicionCamion)
direccion5 = Node("banco3", distancia = 7, string = "Carrera 25 #37-12", parent = posicionCamion)

def calcularPadre(raiz):
    hijos = raiz.children
    if len(hijos) < 2:
        print("No hay suficientes hijos para realizar comparaciones.")
        return raiz

    for i in range(len(hijos) - 1):
        # Comparar distancias y ajustar padres si es necesario
        if hijos[i].distancia > hijos[i + 1].distancia and hijos[i].name == hijos[i + 1].name:
            hijos[i].parent = hijos[i + 1]
            print(f"Se ha cambiado el padre de {hijos[i].name} a {hijos[i + 1].name}")
        elif hijos[i].distancia < hijos[i + 1].distancia and hijos[i].name == hijos[i + 1].name:
            hijos[i + 1].parent = hijos[i]
            print(f"Se ha cambiado el padre de {hijos[i + 1].name} a {hijos[i].name}")
    return raiz.show()

def contarElementos(raiz):
    contador = 1
    if not raiz.children:
        print(f"el nodo {raiz.name} no tiene hijos")
        return contador
    hijos = raiz.children
    for i in range(len(hijos)):
        contador += 1
    return contador

def hijosNivel(raiz):
    niveles = {}
    for nodo in [raiz] + list(raiz.descendants):
        nivel = nodo.depth
        if nivel not in niveles:
            niveles[nivel] = 0
        niveles[nivel] += 1
    return niveles


def rutaDireccion(raiz, nodo):
    return raiz.go_to(nodo)

def buscarDireccion(raiz, stringDireccion):
    descendientes = list(raiz.descendants)
    for descendiente in descendientes:
        if descendiente.string == stringDireccion:
            return True
    print(f"No se encuentra {stringDireccion} en el mapa de direcciones que debe recorrer el camion")
    return False

def impresionRuta(raiz, strFormaImpresion):
    if strFormaImpresion == "con datos":
        return raiz.show(attr_list = ["distancia", "string"])
    elif strFormaImpresion == "sin datos":
        return raiz.hshow()

calcularPadre(posicionCamion)
print(posicionCamion.show())
print(contarElementos(posicionCamion))
hijosNivel(posicionCamion)
rutaDireccion(posicionCamion, direccion4)
buscarDireccion(posicionCamion, "Calle 30 #50-10")
impresionRuta(posicionCamion, "con datos")
impresionRuta(posicionCamion, "sin datos")
# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: [Primera entrega parcial] - Proyecto de Clase
# ===========================================
#Fecha 11/03/2025
#Estudiantes:
#Kevin David Basto Quintero 2222974
#Andres Santiago Culman Sanchez 2241929

class Nodo:
    def __init__(self, dato):
        self.anterior = None
        self.siguiente = None
        self.dato = dato

class ListaDoble:
    def __init__(self, siguiente = None, anterior = None, dato = None):   #Inicializacion vacia de la lista doblemente enlazada
        self.cabeza = None

    def estaVacia(self):
        if self.cabeza == None:                 #Si la cabeza de la lista es nula, la lista está vacía
            return True
        else: return False
    
    def contarElementos(self):
        contador = 0
        nodoActual = self.cabeza
        while nodoActual is not None:           #La condicion del while es que ejecute mientras el nodo actual no sea nulo, es una forma de recorrer la lista
            contador += 1
            nodoActual = nodoActual.siguiente   #El nodo actual se convierte en el siguiente nodo
        return contador
    
    def imprimirLista(self):
        nodoActual = self.cabeza
        while nodoActual is not None:           #La condicion del while es la misma que en el metodo contarElementos
            print(nodoActual.dato, end = " ")
            nodoActual = nodoActual.siguiente
            if nodoActual == self.cabeza:
                break
        print("")                               #Salto de linea

    def insertarInicio(self, dato):
        nuevoNodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
            self.cabeza.siguiente = None
            self.cabeza.anterior = None
        else:
            ultimoNodo = Nodo(self.cabeza.anterior)
            nuevoNodo.siguiente = self.cabeza   #El nuevo nodo apunta (con el apuntador al siguiente) al nodo que estaba al principio
            nuevoNodo.anterior = ultimoNodo     #El nuevo nodo apunta (con el apuntador al anterior) al nodo que estaba al final
            ultimoNodo.siguiente = nuevoNodo    #El nodo que estaba al final apunta (con el apuntador al siguiente) al nuevo nodo
            self.cabeza.anterior = nuevoNodo    #El nodo que estaba al principio apunta (con el apuntador al anterior) al nuevo nodo
            self.cabeza = nuevoNodo             #El nuevo nodo se convierte en el nodo que está al principio
            print(f"El nodo con dato {dato} ha sido insertado al inicio de la lista")
    
    def buscarElemento(self, dato):
        nodoActual = self.cabeza
        while nodoActual is not None:
            if nodoActual.dato == dato:
                return True
            nodoActual = nodoActual.siguiente
        return False
    
    def eliminarNodo(self, dato):
        if not self.cabeza:                     #Manejo de excepcion: lista vacía
            return "EXCEPCIÓN: No se pueden eliminar elementos porque la lista está vacía"
        nodoActual = self.cabeza
        while nodoActual is not None:
            if nodoActual.dato == dato:
                if nodoActual == self.cabeza and nodoActual.siguiente == self.cabeza:
                    self.cabeza = None          #Manejo de excepcion: lista con un unico elemento
                    return "EXCEPCIÓN: El unico nodo en la lista ha sido eliminado"
                else:
                    nodoActual.anterior.siguiente = nodoActual.siguiente    #Asignacion del apuntador del elemento anterior a la variable al siguiente de este
                    nodoActual.siguiente.anterior =  nodoActual.anterior     #Asignacion del apuntador del elemento siguiente a la variable al anterior de este
                    if nodoActual == self.cabeza:
                        self.cabeza = nodoActual.siguiente
                    return "El nodo ha sido eliminado"
            nodoActual = nodoActual.siguiente
            if nodoActual == self.cabeza:       #Manejo de excepcion: dato no encontrado
                break
        return (f"EXCEPCIÓN: Nodo con dato {dato} no encontrado")



listaDoble = ListaDoble()

print(f"Eliminacion del nodo con dato: 1 {listaDoble.eliminarNodo(1)}")

listaDoble.insertarInicio(5)
listaDoble.insertarInicio(4)
listaDoble.insertarInicio(3)
listaDoble.insertarInicio(2)
listaDoble.insertarInicio(1)

listaVacia = bool(listaDoble.estaVacia())
if listaVacia == True:
    print("La lista está vacía")
else: print("La lista no está vacía")

print(f"La cantidad de elementos en la lista es: {listaDoble.contarElementos()}")

print(f"******IMPRESION DE LA LISTA:******")
listaDoble.imprimirLista()

elementoBuscado = listaDoble.buscarElemento(3)
print(f"¿El elemento {3} se encuentra en la lista?")
if elementoBuscado == True:
    print("Sí")
else: print("No")

print(f"Eliminacion del nodo con dato: 3 \n {listaDoble.eliminarNodo(3)}")
print(f"Lista actualizada:")
listaDoble.imprimirLista()
print(f"Eliminacion del nodo con dato: 6 \n {listaDoble.eliminarNodo(6)}")
listaDoble.imprimirLista()
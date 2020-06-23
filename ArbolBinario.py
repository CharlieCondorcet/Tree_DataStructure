
class ArbolBinario:

    # constructor.
    def __init__(self, raiz):
        self.dato = raiz
        self.nivel = 0
        self.hijoIzq = None
        self.hijoDer = None
        self.maxNivel = 0

    # ordena el nodo segun valor y agrega el nivel correspondiente.
    def agregarNodo(self, raizActual, nodo, deserveLevel):
        if(raizActual.dato == nodo.dato):
            return False
        elif(raizActual.dato > nodo.dato):
            if(raizActual.hijoIzq == None):
                raizActual.hijoIzq = nodo
                raizActual.hijoIzq.nivel = deserveLevel+1
                if(self.maxNivel < deserveLevel+1):
                    self.maxNivel = deserveLevel+1
                return True
            else:
                self.agregarNodo(raizActual.hijoIzq, nodo, deserveLevel+1)
        else:
            if(raizActual.hijoDer == None):
                raizActual.hijoDer = nodo
                raizActual.hijoDer.nivel = deserveLevel+1
                if(self.maxNivel < deserveLevel+1):
                    self.maxNivel = deserveLevel+1
                return True
            else:
                self.agregarNodo(raizActual.hijoDer, nodo, deserveLevel+1)

    # impresion de datos inorder.
    def inorder(self, nodoPrincipal):
        if(nodoPrincipal):
            self.inorder(nodoPrincipal.hijoIzq)
            print(
                f"dato: {nodoPrincipal.dato} |con nivel: {nodoPrincipal.nivel} .")
            self.inorder(nodoPrincipal.hijoDer)

    # llamada para impresion.
    def printTree(self, nodoPrincipal):
        if(nodoPrincipal != None):
            self.printArbol("", nodoPrincipal, False)
            return True
        else:
            print("No hay datos")
            return False

    # imprimir arbol completo.
    def printArbol(self, espacio, nodo, tope):
        if (nodo != None):
            print(str(espacio) + ("|--" if (tope) else "\\--") +
                  (str(nodo.dato)+":"+str(nodo.nivel)))
            self.printArbol(espacio + ("|   " if (tope)
                                       else "    "), nodo.hijoIzq, True)
            self.printArbol(espacio + ("|   " if (tope)
                                       else "    "), nodo.hijoDer, False)

            
from Nodo import *
from ArbolBinario import *
import sys


class BinTreeSystem:

    def __init__(self):
        self.arbolBinario = None

    def menu(self):
        print("ingrese una opcion: ")
        print("1.- crear Arbol Binario.")
        print("2.- ingresar Nodo al Arbol Binario.")
        print("3.- imprimir Arbol Binario.")
        print("4.- finaliza programa.")

        opcion = int(input("ingresar opcion:"))
        while (opcion < 1 and opcion > 4):
            opcion = int(input("ingresar una opcion valida:"))
        return opcion

    def crearArbol(self):
        if(self.arbolBinario != None):
            print("ya existe el Arbol Binario.")
        else:
            arbolBin = ArbolBinario(
                int(input("ingrese el valor del nuevo Arbol Binario: ")))
            self.arbolBinario = arbolBin
            print("Arbol Binario creado")

    def agregarNodos(self):
        print("para salir ingrese 9999.")
        valor = None
        verificacion = None
        while (True):
            valor = Nodo(
                int(float(input("ingrese el valor del nuevo Nodo: "))))
            if(valor.dato == 9999):
                print("Saliendo")
                return
            elif(self.arbolBinario != None):
                verificacion = self.arbolBinario.agregarNodo(
                    self.arbolBinario, valor, 0)
                print(verificacion)
                print("Nodo agregado" if (verificacion)
                      else "Nodo no agregado, valor repetido")
            else:
                self.arbolBinario = ArbolBinario(valor.dato)
                print("Arbol Binario creado.")

    def ejecucion(self):
        opcion = self.menu()
        while (True):
            if(opcion == 1):
                self.crearArbol()
            elif(opcion == 2):
                self.agregarNodos()
            elif (opcion == 3):
                self.arbolBinario.printTree(self.arbolBinario)
            else:
                print("saliendo del programa..")
                sys.exit()
            opcion = self.menu()

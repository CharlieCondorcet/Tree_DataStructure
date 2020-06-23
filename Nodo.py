
class Nodo:

    # constructor con atributos privados.
    def __init__(self, datoNuevo):
        self.dato = datoNuevo
        self.nivel = 0
        self.hijoIzq = None
        self.hijoDer = None

    # no hubo encapsulamiento por practicidad del proyecto.
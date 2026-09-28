"""Implementación manual de una cola para administrar novedades policiales utilizando el principio FIFO."""

class ColaNovedades:
    
    def __init__(self):
        self.__elementos = []

    # Agregar un elemento al final de la cola
    def agregar(self, novedad):
        self.__elementos.append(novedad)

    # Eliminar y devolver el primer elemento de la cola
    def eliminar(self):
        if self.esta_vacia():
            return None

        return self.__elementos.pop(0)

    # Consultar el siguiente elemento sin eliminarlo
    def consultar_siguiente(self):
        if self.esta_vacia():
            return None

        return self.__elementos[0]

    # Verificar si la cola está vacía
    def esta_vacia(self):
        return len(self.__elementos) == 0

    # Consultar la cantidad de elementos
    def cantidad(self):
        return len(self.__elementos)
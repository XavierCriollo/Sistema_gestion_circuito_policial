class Subcircuito:
    def __init__(self, nombre, vehiculo):
        self.__nombre = nombre
        self.__vehiculo = vehiculo
        self.__turnos = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_vehiculo(self):
        return self.__vehiculo

    def set_vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    def get_turnos(self):
        return self.__turnos

    def agregar_turno(self, turno):
        self.__turnos.append(turno)
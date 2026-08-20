class ServidorPolicial:
    def __init__(self, nombre, identificacion, grado, estado):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__grado = grado
        self.__estado = estado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def get_grado(self):
        return self.__grado

    def set_grado(self, grado):
        self.__grado = grado

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado
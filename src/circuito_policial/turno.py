class Turno:
    def __init__(self, nombre, hora_inicio, hora_fin):
        self.__nombre = nombre
        self.__hora_inicio = hora_inicio
        self.__hora_fin = hora_fin
        self.__servidores = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_hora_inicio(self):
        return self.__hora_inicio

    def set_hora_inicio(self, hora_inicio):
        self.__hora_inicio = hora_inicio

    def get_hora_fin(self):
        return self.__hora_fin

    def set_hora_fin(self, hora_fin):
        self.__hora_fin = hora_fin

    def get_servidores(self):
        return self.__servidores
    
    def agregar_servidor(self, servidor):
        if len(self.__servidores) < 2:
            self.__servidores.append(servidor)
            print("Servidor agregado al turno.")
        else:
            print("El turno ya tiene el número máximo de servidores.")
            
    def mostrar_servidores(self):
        print(f"\nTurno: {self.__nombre}")
        print(f"Hora de inicio: {self.__hora_inicio} - Hora de fin: {self.__hora_fin}")
        
        for servidor in self.__servidores:
            print(
                servidor.get_grado(),
                servidor.get_nombre(),
            )
    
    def eliminar_servidor(self, servidor):
        if servidor in self.__servidores:
            self.__servidores.remove(servidor)
            print("Servidor eliminado del turno.")
        else:
            print("El servidor no está asignado a este turno.")
            
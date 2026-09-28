from circuito_policial.cola_novedades import ColaNovedades
from circuito_policial.servidor_repository import ServidorRepository


class GestionNovedades:

    def __init__(self, repository: ServidorRepository):
        self.__repository = repository
        self.__cola = ColaNovedades()

    def registrar_novedad(self, novedad):
        """Agrega una novedad a la cola."""
        self.__cola.agregar(novedad)

    def atender_novedad(self):
        """Atiende la novedad más antigua."""
        return self.__cola.eliminar()

    def consultar_siguiente(self):
        """Consulta la próxima novedad sin eliminarla."""
        return self.__cola.consultar_siguiente()

    def cantidad_novedades(self):
        return self.__cola.cantidad()

    def cola_vacia(self):
        return self.__cola.esta_vacia()

    def listar_servidores(self):
        """
        Utiliza Repository para obtener
        los servidores almacenados.
        """
        return self.__repository.listar()
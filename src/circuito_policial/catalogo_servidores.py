from typing import Generic, TypeVar

from pydantic import ValidationError

from circuito_policial.servidor_policial import ServidorPolicial
from circuito_policial.validaciones import ServidorPolicialData


# T representa un tipo genérico que debe ser
# ServidorPolicial o una clase que herede de ella.
T = TypeVar("T", bound=ServidorPolicial)


class CatalogoServidores(Generic[T]):

    def __init__(self):
        # Lista principal de servidores policiales
        self.__servidores: list[T] = []

        # Diccionario para buscar servidores por identificación
        self.__servidores_por_id: dict[str, T] = {}

        # Set para controlar identificaciones únicas
        self.__identificaciones: set[str] = set()

    # --------------------------------------------------
    # AGREGAR SERVIDOR
    # --------------------------------------------------

    def agregar_servidor(self, servidor: T) -> bool:

        identificacion = servidor.get_identificacion()

        if identificacion in self.__identificaciones:
            print(
                f"No se puede agregar. La identificación "
                f"{identificacion} ya existe."
            )
            return False

        self.__servidores.append(servidor)
        self.__servidores_por_id[identificacion] = servidor
        self.__identificaciones.add(identificacion)

        print(
            f"Servidor {servidor.get_nombre()} "
            f"agregado correctamente."
        )

        return True

    # --------------------------------------------------
    # BUSCAR SERVIDOR
    # --------------------------------------------------

    def buscar_servidor(self, identificacion: str):

        servidor = self.__servidores_por_id.get(identificacion)

        if servidor is None:
            print(
                f"No se encontró un servidor con la identificación "
                f"{identificacion}."
            )
            return None

        return servidor

    # --------------------------------------------------
    # LISTAR SERVIDORES
    # --------------------------------------------------

    def listar_servidores(self) -> list[T]:

        return self.__servidores.copy()

    # --------------------------------------------------
    # ACTUALIZAR SERVIDOR
    # --------------------------------------------------

    def actualizar_servidor(
        self,
        identificacion: str,
        nombre: str,
        grado: str,
        estado: str
    ) -> bool:

        servidor = self.__servidores_por_id.get(identificacion)

        if servidor is None:
            print(
                f"No se puede actualizar. La identificación "
                f"{identificacion} no existe."
            )
            return False

        try:
            datos_validados = ServidorPolicialData(
                nombre=nombre,
                identificacion=identificacion,
                grado=grado,
                estado=estado
            )

        except ValidationError:
            print(
                "No se puede actualizar. "
                "Los datos ingresados no son válidos."
            )
            return False

        servidor.set_nombre(datos_validados.nombre)
        servidor.set_grado(datos_validados.grado)
        servidor.set_estado(datos_validados.estado)

        print(
            f"Servidor {identificacion} "
            f"actualizado correctamente."
        )

        return True

    # --------------------------------------------------
    # ELIMINAR SERVIDOR
    # --------------------------------------------------

    def eliminar_servidor(self, identificacion: str) -> bool:

        servidor = self.__servidores_por_id.get(identificacion)

        if servidor is None:
            print(
                f"No se puede eliminar. La identificación "
                f"{identificacion} no existe."
            )
            return False

        # Eliminar de la lista
        self.__servidores.remove(servidor)

        # Eliminar del diccionario
        del self.__servidores_por_id[identificacion]

        # Eliminar la identificación del set
        self.__identificaciones.remove(identificacion)

        print(
            f"Servidor {identificacion} "
            f"eliminado correctamente."
        )

        return True
    
    
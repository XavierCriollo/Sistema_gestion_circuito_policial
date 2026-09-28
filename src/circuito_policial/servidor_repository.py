from circuito_policial.base_datos import BaseDatos
from circuito_policial.cola_novedades import ColaNovedades


class ServidorRepository:

    def __init__(self, base_datos: BaseDatos):
        self.__base_datos = base_datos
        self.__cola_novedades = ColaNovedades()

    # --------------------------------------------------
    # CREATE
    # --------------------------------------------------

    def guardar(
        self,
        identificacion: str,
        nombre: str,
        tipo: str,
        grado: str,
        estado: str
    ) -> bool:

        resultado = self.__base_datos.guardar_servidor(
            identificacion,
            nombre,
            tipo,
            grado,
            estado
        )

        if resultado:
            self.__cola_novedades.agregar(
                f"Servidor {identificacion} registrado"
            )

        return resultado

    # --------------------------------------------------
    # READ - BUSCAR
    # --------------------------------------------------

    def buscar(self, identificacion: str):

        return self.__base_datos.buscar_servidor(
            identificacion
        )

    # --------------------------------------------------
    # READ - LISTAR
    # --------------------------------------------------

    def listar(self):

        return self.__base_datos.listar_servidores()

    # --------------------------------------------------
    # UPDATE
    # --------------------------------------------------

    def actualizar(
        self,
        identificacion: str,
        nombre: str,
        tipo: str,
        grado: str,
        estado: str
    ) -> bool:

        resultado = self.__base_datos.actualizar_servidor(
            identificacion,
            nombre,
            tipo,
            grado,
            estado
        )

        if resultado:
            self.__cola_novedades.agregar(
                f"Servidor {identificacion} actualizado"
            )

        return resultado

    # --------------------------------------------------
    # DELETE
    # --------------------------------------------------

    def eliminar(self, identificacion: str) -> bool:

        resultado = self.__base_datos.eliminar_servidor(
            identificacion
        )

        if resultado:
            self.__cola_novedades.agregar(
                f"Servidor {identificacion} eliminado"
            )

        return resultado

    # --------------------------------------------------
    # COLA DE NOVEDADES
    # --------------------------------------------------

    def siguiente_novedad(self):

        return self.__cola_novedades.consultar_siguiente()

    def atender_novedad(self):

        return self.__cola_novedades.eliminar()

    def cantidad_novedades(self) -> int:

        return self.__cola_novedades.cantidad()

    def novedades_pendientes(self) -> bool:

        return not self.__cola_novedades.esta_vacia()
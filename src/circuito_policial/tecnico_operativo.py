from circuito_policial.servidor_policial import ServidorPolicial


class TecnicoOperativo(ServidorPolicial):

    GRADOS_TECNICO_OPERATIVOS = [
        "Policia",
        "Cabo Segundo",
        "Cabo Primero",
        "Sargento Segundo",
        "Sargento Primero",
        "Suboficial Segundo",
        "Suboficial Primero",
        "Suboficial Mayor"
    ]

    def __init__(self, nombre, identificacion, grado, estado):
        if grado not in self.GRADOS_TECNICO_OPERATIVOS:
            raise ValueError(
                "El grado no corresponde a un Tecnico Operativo"
            )

        super().__init__(nombre, identificacion, grado, estado)
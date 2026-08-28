from circuito_policial.servidor_policial import ServidorPolicial


class Directivo(ServidorPolicial):

    GRADOS_DIRECTIVOS = [
        "Subteniente",
        "Teniente",
        "Capitan",
        "Mayor",
        "Teniente Coronel",
        "Coronel",
        "General"
    ]

    def __init__(self, nombre, identificacion, grado, estado):
        if grado not in self.GRADOS_DIRECTIVOS:
            raise ValueError("El grado no corresponde a un Directivo")

        super().__init__(nombre, identificacion, grado, estado)
        
    def mostrar_funcion(self):
        return "Direccion, supervision y mando"   
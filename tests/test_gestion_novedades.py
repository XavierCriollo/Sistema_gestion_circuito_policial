from circuito_policial.base_datos import BaseDatos
from circuito_policial.servidor_repository import ServidorRepository
from circuito_policial.gestion_novedades import GestionNovedades


def test_gestion_cola_novedades(tmp_path):
    ruta_db = tmp_path / "test.db"

    base_datos = BaseDatos(str(ruta_db))
    base_datos.crear_tabla_servidores()

    repository = ServidorRepository(base_datos)
    gestion = GestionNovedades(repository)

    # La cola debe iniciar vacía
    assert gestion.cola_vacia() is True
    assert gestion.cantidad_novedades() == 0

    # Agregar novedades
    gestion.registrar_novedad("Robo reportado")
    gestion.registrar_novedad("Accidente de tránsito")

    assert gestion.cantidad_novedades() == 2

    # FIFO: la primera en entrar debe ser la primera en salir
    assert gestion.consultar_siguiente() == "Robo reportado"
    assert gestion.atender_novedad() == "Robo reportado"

    # Debe quedar la segunda novedad
    assert gestion.consultar_siguiente() == "Accidente de tránsito"
    assert gestion.cantidad_novedades() == 1


def test_gestion_utiliza_repository(tmp_path):
    ruta_db = tmp_path / "test.db"

    base_datos = BaseDatos(str(ruta_db))
    base_datos.crear_tabla_servidores()

    repository = ServidorRepository(base_datos)
    gestion = GestionNovedades(repository)

    servidores = gestion.listar_servidores()

    assert isinstance(servidores, list)
    assert servidores == []
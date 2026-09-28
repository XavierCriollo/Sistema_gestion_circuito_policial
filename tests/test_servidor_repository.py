from circuito_policial.base_datos import BaseDatos
from circuito_policial.servidor_repository import ServidorRepository


def crear_repository(tmp_path):
    ruta_bd = tmp_path / "test_circuito.db"

    base_datos = BaseDatos(str(ruta_bd))
    base_datos.crear_tabla_servidores()

    return ServidorRepository(base_datos)


def test_guardar_servidor_y_generar_novedad(tmp_path):
    repository = crear_repository(tmp_path)

    resultado = repository.guardar(
        "T9001",
        "Servidor Prueba",
        "TecnicoOperativo",
        "Cabo Primero",
        "Disponible"
    )

    assert resultado is True
    assert repository.cantidad_novedades() == 1
    assert repository.siguiente_novedad() == "Servidor T9001 registrado"


def test_buscar_servidor(tmp_path):
    repository = crear_repository(tmp_path)

    repository.guardar(
        "T9002",
        "Servidor Busqueda",
        "TecnicoOperativo",
        "Cabo Segundo",
        "Disponible"
    )

    servidor = repository.buscar("T9002")

    assert servidor is not None
    assert servidor[0] == "T9002"
    assert servidor[1] == "Servidor Busqueda"


def test_actualizar_servidor(tmp_path):
    repository = crear_repository(tmp_path)

    repository.guardar(
        "T9003",
        "Servidor Original",
        "TecnicoOperativo",
        "Cabo Segundo",
        "Disponible"
    )

    resultado = repository.actualizar(
        "T9003",
        "Servidor Actualizado",
        "TecnicoOperativo",
        "Cabo Primero",
        "Servicio"
    )

    assert resultado is True

    servidor = repository.buscar("T9003")

    assert servidor[1] == "Servidor Actualizado"
    assert servidor[3] == "Cabo Primero"
    assert servidor[4] == "Servicio"


def test_eliminar_servidor(tmp_path):
    repository = crear_repository(tmp_path)

    repository.guardar(
        "T9004",
        "Servidor Eliminar",
        "TecnicoOperativo",
        "Policia",
        "Disponible"
    )

    resultado = repository.eliminar("T9004")

    assert resultado is True
    assert repository.buscar("T9004") is None


def test_cola_repository_fifo(tmp_path):
    repository = crear_repository(tmp_path)

    repository.guardar(
        "T9005",
        "Servidor FIFO",
        "TecnicoOperativo",
        "Policia",
        "Disponible"
    )

    repository.actualizar(
        "T9005",
        "Servidor FIFO",
        "TecnicoOperativo",
        "Cabo Segundo",
        "Servicio"
    )

    assert repository.cantidad_novedades() == 2

    assert (
        repository.atender_novedad()
        == "Servidor T9005 registrado"
    )

    assert (
        repository.atender_novedad()
        == "Servidor T9005 actualizado"
    )

    assert repository.novedades_pendientes() is False
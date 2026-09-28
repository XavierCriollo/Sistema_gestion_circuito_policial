from circuito_policial.cola_novedades import ColaNovedades


def test_cola_inicialmente_vacia():
    cola = ColaNovedades()

    assert cola.esta_vacia() is True
    assert cola.cantidad() == 0


def test_agregar_novedades():
    cola = ColaNovedades()

    cola.agregar("Robo reportado")
    cola.agregar("Accidente de tránsito")

    assert cola.cantidad() == 2
    assert cola.esta_vacia() is False


def test_consultar_siguiente():
    cola = ColaNovedades()

    cola.agregar("Robo reportado")
    cola.agregar("Accidente de tránsito")

    assert cola.consultar_siguiente() == "Robo reportado"


def test_eliminar_novedad():
    cola = ColaNovedades()

    cola.agregar("Robo reportado")
    cola.agregar("Accidente de tránsito")

    novedad = cola.eliminar()

    assert novedad == "Robo reportado"
    assert cola.cantidad() == 1


def test_funcionamiento_fifo():
    cola = ColaNovedades()

    cola.agregar("Robo reportado")
    cola.agregar("Accidente de tránsito")
    cola.agregar("Persona sospechosa")

    assert cola.eliminar() == "Robo reportado"
    assert cola.eliminar() == "Accidente de tránsito"
    assert cola.eliminar() == "Persona sospechosa"
    assert cola.esta_vacia() is True
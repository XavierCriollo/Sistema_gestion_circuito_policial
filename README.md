# Sistema de Gestión de Circuito Policial

## Descripción

Sistema desarrollado en **Python** para representar y gestionar elementos básicos de un circuito policial.

El proyecto ha sido desarrollado de forma incremental aplicando **Programación Orientada a Objetos**, colecciones, genéricos, validación de datos, persistencia en SQLite, interfaz gráfica, tipos de datos abstractos lineales, patrones de diseño y pruebas unitarias.

## Características principales

- Gestión de servidores policiales.
- Clasificación en `Directivo` y `TecnicoOperativo`.
- Validación de grados según el tipo de servidor.
- Gestión de vehículos, turnos y subcircuitos.
- Catálogo de servidores mediante colecciones.
- Validación de datos con Pydantic.
- Persistencia de información en SQLite.
- Interfaz gráfica desarrollada con Flet.
- Operaciones CRUD desde la interfaz gráfica.
- Gestión de novedades mediante una cola FIFO.
- Implementación del patrón Repository.
- Pruebas unitarias mediante pytest.

## Conceptos aplicados

### Programación Orientada a Objetos

- **Encapsulación:** atributos privados mediante métodos `get` y `set`.
- **Composición:** relaciones entre subcircuitos, vehículos y turnos.
- **Herencia:** `Directivo` y `TecnicoOperativo` heredan de `ServidorPolicial`.
- **Abstracción:** `ServidorPolicial` funciona como clase base abstracta.
- **Polimorfismo:** cada tipo de servidor implementa su propio comportamiento.

### Colecciones y genéricos

El catálogo de servidores utiliza tres tipos de colecciones:

- `list`: almacena y permite listar los servidores.
- `dict`: permite buscar servidores mediante su identificación.
- `set`: controla que las identificaciones sean únicas.

La clase `CatalogoServidores` utiliza `Generic` y `TypeVar` para trabajar con objetos de tipo `ServidorPolicial` y sus clases derivadas.

El catálogo permite realizar operaciones de agregar, buscar, listar, actualizar y eliminar servidores.

### Validación de datos

Los datos ingresados son validados mediante **Pydantic** antes de ser procesados por el sistema.

Esto permite controlar la información ingresada y evitar que datos incorrectos sean almacenados o utilizados por la aplicación.

### Persistencia y CRUD

El sistema utiliza **SQLite** para almacenar de forma persistente la información de los servidores policiales.

Se implementaron las operaciones CRUD:

- **Create:** registrar servidores.
- **Read:** buscar y listar servidores.
- **Update:** actualizar información.
- **Delete:** eliminar servidores.

### Interfaz gráfica y eventos

La interfaz fue desarrollada con **Flet** e implementa las operaciones:

- Guardar servidor.
- Buscar servidor.
- Listar servidores.
- Actualizar servidor.
- Eliminar servidor.

Los botones y controles de selección utilizan **manejo de eventos** para ejecutar las diferentes operaciones.

La interfaz se encuentra conectada con SQLite, permitiendo que los cambios realizados por el usuario se reflejen en los datos almacenados y en la tabla de servidores registrados.

### Cola FIFO

Para la gestión de novedades se implementó la clase `ColaNovedades`, utilizando una estructura de datos lineal basada en el principio **FIFO (First In, First Out)**.

La cola permite:

- Registrar novedades.
- Consultar la siguiente novedad.
- Atender y eliminar la novedad más antigua.
- Consultar la cantidad de novedades pendientes.
- Verificar si la cola está vacía.

La estructura FIFO garantiza que la primera novedad registrada sea también la primera en ser atendida.

### Patrón Repository

Se implementó el patrón de diseño **Repository** mediante la clase `ServidorRepository`.

Este patrón permite separar el acceso y manejo de los datos de la lógica principal de la aplicación, utilizando `BaseDatos` como mecanismo de persistencia en SQLite.

La clase `GestionNovedades` integra la gestión de la cola FIFO con el Repository, manteniendo separadas las responsabilidades de cada componente.

### Pruebas unitarias

Se implementaron **pruebas unitarias con pytest** para verificar automáticamente el correcto funcionamiento de las principales operaciones desarrolladas durante la Semana 7.

Las pruebas comprueban:

- Estado inicial de la cola.
- Registro de novedades.
- Consulta de la siguiente novedad.
- Eliminación de novedades.
- Funcionamiento FIFO.
- Operaciones mediante `ServidorRepository`.
- Integración mediante `GestionNovedades`.

Actualmente el proyecto cuenta con **12 pruebas unitarias aprobadas**.

## Tecnologías

- Python 3
- Flet
- Pydantic
- SQLite
- pytest
- uv
- Git y GitHub
- Visual Studio Code
- UML con Draw.io

## Ejecución

Desde la raíz del proyecto, instalar las dependencias:

```bash
uv sync
```

Ejecutar la interfaz gráfica:

```bash
uv run src/circuito_policial/interfaz.py
```

Ejecutar las pruebas unitarias:

```bash
PYTHONPATH=src uv run pytest -v
```

## Estructura principal

```text
circuito_policial/
│
├── main.py
├── README.md
├── pyproject.toml
├── uv.lock
│
├── src/
│   └── circuito_policial/
│       ├── __init__.py
│       ├── servidor_policial.py
│       ├── directivo.py
│       ├── tecnico_operativo.py
│       ├── vehiculo.py
│       ├── turno.py
│       ├── subcircuito.py
│       ├── catalogo_servidores.py
│       ├── validaciones.py
│       ├── base_datos.py
│       ├── interfaz.py
│       ├── cola_novedades.py
│       ├── servidor_repository.py
│       └── gestion_novedades.py
│
└── tests/
    ├── test_cola_novedades.py
    ├── test_gestion_novedades.py
    └── test_servidor_repository.py
```

## Desarrollo incremental

El proyecto ha incorporado progresivamente los siguientes conceptos:

- **Semanas iniciales:** encapsulación, composición, herencia, abstracción y polimorfismo.
- **Semana 5:** colecciones, genéricos y catálogo de servidores.
- **Semana 6:** interfaz gráfica, operaciones CRUD, manejo de eventos, validación con Pydantic y persistencia mediante SQLite.
- **Semana 7:** cola FIFO, patrón Repository, integración de novedades y pruebas unitarias mediante pytest.

## Estado del proyecto

El sistema cuenta actualmente con gestión de servidores policiales, validación de datos, almacenamiento mediante SQLite, interfaz gráfica con operaciones CRUD y gestión de novedades mediante una cola FIFO.

El proyecto integra **Programación Orientada a Objetos, colecciones, genéricos, Pydantic, SQLite, Flet, tipos de datos abstractos lineales, patrón Repository y pruebas unitarias con pytest**, manteniendo una estructura modular preparada para futuras ampliaciones.
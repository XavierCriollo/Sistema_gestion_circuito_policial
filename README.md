# Sistema de Gestión de Circuito Policial

## Descripción

Sistema desarrollado en **Python** para representar y gestionar elementos básicos de un circuito policial.

El proyecto ha sido desarrollado de forma incremental aplicando Programación Orientada a Objetos, colecciones, genéricos, validación de datos, persistencia en SQLite e interfaz gráfica.

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

### Interfaz gráfica y eventos

La interfaz fue desarrollada con **Flet** e implementa las operaciones:

- Guardar servidor.
- Buscar servidor.
- Listar servidores.
- Actualizar servidor.
- Eliminar servidor.

Los botones y controles de selección utilizan eventos para ejecutar las diferentes operaciones.

Los datos ingresados son validados con **Pydantic** antes de ser procesados.

## Tecnologías

- Python 3
- Flet
- Pydantic
- SQLite
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

## Estructura principal

```text
circuito_policial/
│
├── main.py
├── README.md
├── pyproject.toml
├── circuito_policial.db
│
└── src/
    └── circuito_policial/
        ├── __init__.py
        ├── servidor_policial.py
        ├── directivo.py
        ├── tecnico_operativo.py
        ├── vehiculo.py
        ├── turno.py
        ├── subcircuito.py
        ├── catalogo_servidores.py
        ├── validaciones.py
        ├── base_datos.py
        └── interfaz.py
```

## Estado del proyecto

El sistema cuenta actualmente con un catálogo de servidores policiales, validación de datos, almacenamiento mediante SQLite e interfaz gráfica con operaciones CRUD.

El proyecto integra los conceptos desarrollados durante las diferentes etapas manteniendo una estructura preparada para futuras ampliaciones.
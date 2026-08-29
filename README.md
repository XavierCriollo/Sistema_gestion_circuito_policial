# Sistema de Gestión de Circuito Policial

## Descripción

El **Sistema de Gestión de Circuito Policial** es un proyecto desarrollado en **Python** con el objetivo de modelar, mediante Programación Orientada a Objetos (POO), los elementos que intervienen en la organización y funcionamiento de un circuito policial, para lo cual se crearon clases para representar elementos del sistema como servidor policial, vehículo, turno, subcircuito, directivo y técnico operativo.

Se aplicó encapsulación mediante atributos privados, getters y setters; composición para relacionar los objetos; y herencia, donde ServidorPolicial es la clase padre de Directivo y TecnicoOperativo, para lo que dicha solución ha sido desarrollada de forma incremental, incorporando encapsulación, composición, herencia, clases abstractas y polimorfismo.

## Objetivo

Desarrollar una solución orientada a objetos que permita representar de forma estructurada los componentes principales de un circuito policial, aplicando conceptos fundamentales de diseño y programación.

## Características principales

- Gestión de servidores policiales.
- Clasificación en `Directivo` y `TecnicoOperativo`.
- Gestión de vehículos y turnos de servicio.
- Organización de información mediante subcircuitos.
- Validación de grados según el tipo de servidor policial.
- Modelado de relaciones entre las diferentes clases.

## Conceptos de POO aplicados

El proyecto implementa los siguientes conceptos:

- **Encapsulación:** protección de atributos mediante métodos `get` y `set`.
- **Composición:** relación entre objetos como subcircuitos, vehículos y turnos.
- **Herencia:** `Directivo` y `TecnicoOperativo` heredan de `ServidorPolicial`.
- **Abstracción:** `ServidorPolicial` funciona como clase base abstracta.
- **Polimorfismo:** cada tipo de servidor policial implementa su propio comportamiento.

## Tecnologías

- Python 3
- Git y GitHub
- Visual Studio Code
- UML con Draw.io

## Ejecución

Desde la raíz del proyecto:

```bash
uv run main.py
---

## Estructura general del proyecto

```text
circuito_policial/
│
├── main.py
├── README.md
├── pyproject.toml
│
└── src/
    └── circuito_policial/
        ├── __init__.py
        ├── servidor_policial.py
        ├── directivo.py
        ├── tecnico_operativo.py
        ├── vehiculo.py
        ├── turno.py
        └── subcircuito.py
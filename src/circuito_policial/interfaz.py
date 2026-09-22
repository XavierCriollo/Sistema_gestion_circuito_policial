import flet as ft
from pydantic import ValidationError

from circuito_policial.base_datos import BaseDatos
from circuito_policial.validaciones import ServidorPolicialData


def main(page: ft.Page):

    # Configuración de la ventana
    page.title = "Sistema de Gestión de Circuito Policial"
    page.padding = 30

    # Base de datos
    base_datos = BaseDatos()
    base_datos.crear_tabla_servidores()

    # Título
    titulo = ft.Text(
        "Sistema de Gestión de Circuito Policial",
        size=26,
        weight=ft.FontWeight.BOLD,
    )

    subtitulo = ft.Text(
        "Registro de Servidores Policiales",
        size=18,
        weight=ft.FontWeight.BOLD,
    )

    # Catálogo de grados
    grados_directivos = [
        "Subteniente",
        "Teniente",
        "Capitan",
        "Mayor",
        "Teniente Coronel",
        "Coronel",
        "General",
    ]

    grados_tecnicos = [
        "Policia",
        "Cabo Segundo",
        "Cabo Primero",
        "Sargento Segundo",
        "Sargento Primero",
        "Suboficial Segundo",
        "Suboficial Primero",
        "Suboficial Mayor",
    ]

    # Campos del formulario
    identificacion = ft.TextField(
        label="Identificación",
        width=400,
    )

    nombre = ft.TextField(
        label="Nombre completo",
        width=400,
    )

    # Dropdown de grado
    grado = ft.Dropdown(
        label="Grado",
        width=400,
        options=[],
    )

    # Cambiar grados según el tipo de servidor
    def cambiar_tipo(e):

        grado.value = None

        if tipo.value == "Directivo":
            grado.options = [
                ft.DropdownOption(g)
                for g in grados_directivos
            ]

        elif tipo.value == "TecnicoOperativo":
            grado.options = [
                ft.DropdownOption(g)
                for g in grados_tecnicos
            ]

        else:
            grado.options = []

        grado.update()

    # Tipo de servidor
    tipo = ft.Dropdown(
        label="Tipo de servidor",
        width=400,
        options=[
            ft.DropdownOption("Directivo"),
            ft.DropdownOption("TecnicoOperativo"),
        ],
        on_select=cambiar_tipo,
    )

    # Estado
    estado = ft.Dropdown(
        label="Estado",
        width=400,
        options=[
            ft.DropdownOption("Disponible"),
            ft.DropdownOption("Servicio"),
        ],
    )

    # Mensaje para el usuario
    mensaje = ft.Text("")

    # Evento del botón Guardar
    def guardar_servidor(e):

        try:
            # Validar datos con Pydantic
            datos = ServidorPolicialData(
                identificacion=identificacion.value,
                nombre=nombre.value,
                grado=grado.value,
                estado=estado.value,
            )

            # Validar que se seleccione tipo
            if tipo.value is None:
                mensaje.value = "Debe seleccionar el tipo de servidor."
                page.update()
                return

            # Guardar en SQLite
            base_datos.guardar_servidor(
                datos.identificacion,
                datos.nombre,
                tipo.value,
                datos.grado,
                datos.estado,
            )

            mensaje.value = "Servidor guardado correctamente."

            # Limpiar formulario
            identificacion.value = ""
            nombre.value = ""
            tipo.value = None
            grado.value = None
            grado.options = []
            estado.value = None

        except ValidationError:
            mensaje.value = (
                "Error de validación. "
                "Verifique que todos los campos estén completos."
            )

        except Exception as error:
            mensaje.value = f"Error: {error}"

        page.update()

    # Botón Guardar
    boton_guardar = ft.Button(
        content="Guardar",
        on_click=guardar_servidor,
    )

    # Agregar controles a la página
    page.add(
        titulo,
        ft.Divider(),
        subtitulo,
        identificacion,
        nombre,
        tipo,
        grado,
        estado,
        boton_guardar,
        mensaje,
    )


ft.run(main)
import flet as ft
from pydantic import ValidationError

from circuito_policial.base_datos import BaseDatos
from circuito_policial.validaciones import ServidorPolicialData


def main(page: ft.Page):

    # ---------------------------------------------------------
    # CONFIGURACIÓN DE LA VENTANA
    # ---------------------------------------------------------

    page.title = "Sistema de Gestión de Circuito Policial"
    page.padding = 30
    page.scroll = ft.ScrollMode.AUTO

    # ---------------------------------------------------------
    # BASE DE DATOS
    # ---------------------------------------------------------

    base_datos = BaseDatos()
    base_datos.crear_tabla_servidores()

    # ---------------------------------------------------------
    # TÍTULOS
    # ---------------------------------------------------------

    titulo = ft.Text(
        "Sistema de Gestión de Circuito Policial",
        size=28,
        weight=ft.FontWeight.BOLD,
    )

    subtitulo = ft.Text(
        "Registro de Servidores Policiales",
        size=20,
        weight=ft.FontWeight.BOLD,
    )

    # ---------------------------------------------------------
    # CAMPOS DEL FORMULARIO
    # ---------------------------------------------------------

    identificacion = ft.TextField(
        label="Identificación",
        width=430,
    )

    nombre = ft.TextField(
        label="Nombre completo",
        width=430,
    )

    # ---------------------------------------------------------
    # DROPDOWN DE GRADO
    # ---------------------------------------------------------

    grado = ft.Dropdown(
        label="Grado",
        width=430,
        options=[],
    )

    # ---------------------------------------------------------
    # CAMBIAR GRADOS SEGÚN TIPO DE SERVIDOR
    # ---------------------------------------------------------

    def cambiar_tipo(e):

        grado.value = None

        if tipo.value == "Directivo":

            grado.options = [
                ft.DropdownOption("Subteniente"),
                ft.DropdownOption("Teniente"),
                ft.DropdownOption("Capitan"),
                ft.DropdownOption("Mayor"),
                ft.DropdownOption("Teniente Coronel"),
                ft.DropdownOption("Coronel"),
                ft.DropdownOption("General"),
            ]

        elif tipo.value == "TecnicoOperativo":

            grado.options = [
                ft.DropdownOption("Policia"),
                ft.DropdownOption("Cabo Segundo"),
                ft.DropdownOption("Cabo Primero"),
                ft.DropdownOption("Sargento Segundo"),
                ft.DropdownOption("Sargento Primero"),
                ft.DropdownOption("Suboficial Segundo"),
                ft.DropdownOption("Suboficial Primero"),
                ft.DropdownOption("Suboficial Mayor"),
            ]

        else:
            grado.options = []

        page.update()

    # ---------------------------------------------------------
    # DROPDOWN TIPO DE SERVIDOR
    # ---------------------------------------------------------

    tipo = ft.Dropdown(
        label="Tipo de servidor",
        width=430,
        options=[
            ft.DropdownOption("Directivo"),
            ft.DropdownOption("TecnicoOperativo"),
        ],
        on_select=cambiar_tipo,
    )

    # ---------------------------------------------------------
    # DROPDOWN ESTADO
    # ---------------------------------------------------------

    estado = ft.Dropdown(
        label="Estado",
        width=430,
        options=[
            ft.DropdownOption("Disponible"),
            ft.DropdownOption("Servicio"),
        ],
    )

    # ---------------------------------------------------------
    # MENSAJE PARA EL USUARIO
    # ---------------------------------------------------------

    mensaje = ft.Text("")

    # ---------------------------------------------------------
    # TABLA DE SERVIDORES
    # ---------------------------------------------------------

    tabla_servidores = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Identificación")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Grado")),
            ft.DataColumn(ft.Text("Estado")),
        ],
        rows=[],
    )

    # ---------------------------------------------------------
    # CARGAR SERVIDORES DESDE SQLITE
    # ---------------------------------------------------------

    def cargar_servidores():

        servidores = base_datos.listar_servidores()

        tabla_servidores.rows.clear()

        for servidor in servidores:

            tabla_servidores.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(servidor[0])),
                        ft.DataCell(ft.Text(servidor[1])),
                        ft.DataCell(ft.Text(servidor[2])),
                        ft.DataCell(ft.Text(servidor[3])),
                        ft.DataCell(ft.Text(servidor[4])),
                    ]
                )
            )

    # ---------------------------------------------------------
    # LIMPIAR FORMULARIO
    # ---------------------------------------------------------

    def limpiar_formulario():

        identificacion.value = ""
        nombre.value = ""
        tipo.value = None
        grado.value = None
        grado.options = []
        estado.value = None

    # ---------------------------------------------------------
    # GUARDAR SERVIDOR
    # CREATE
    # ---------------------------------------------------------

    def guardar_servidor(e):

        try:

            if tipo.value is None:
                mensaje.value = "Seleccione el tipo de servidor."
                page.update()
                return

            datos = ServidorPolicialData(
                identificacion=identificacion.value,
                nombre=nombre.value,
                grado=grado.value,
                estado=estado.value,
            )

            base_datos.guardar_servidor(
                datos.identificacion,
                datos.nombre,
                tipo.value,
                datos.grado,
                datos.estado,
            )

            mensaje.value = "Servidor guardado correctamente."

            limpiar_formulario()

            # Actualizar tabla
            cargar_servidores()

        except ValidationError:

            mensaje.value = (
                "Error de validación. "
                "Verifique que todos los campos estén completos."
            )

        except Exception as error:

            mensaje.value = f"Error: {error}"

        page.update()

    # ---------------------------------------------------------
    # BUSCAR SERVIDOR
    # READ
    # ---------------------------------------------------------

    def buscar_servidor(e):

        if not identificacion.value:
            mensaje.value = "Ingrese una identificación para buscar."
            page.update()
            return

        servidor = base_datos.buscar_servidor(
            identificacion.value
        )

        if servidor is None:
            mensaje.value = "Servidor no encontrado."
            page.update()
            return

        identificacion.value = servidor[0]
        nombre.value = servidor[1]
        tipo.value = servidor[2]

        # Cargar los grados según el tipo encontrado
        cambiar_tipo(None)

        grado.value = servidor[3]
        estado.value = servidor[4]

        mensaje.value = "Servidor encontrado correctamente."

        page.update()

    # ---------------------------------------------------------
    # ACTUALIZAR SERVIDOR
    # UPDATE
    # ---------------------------------------------------------

    def actualizar_servidor(e):

        try:

            if not identificacion.value:
                mensaje.value = (
                    "Ingrese la identificación del servidor."
                )
                page.update()
                return

            if tipo.value is None:
                mensaje.value = "Seleccione el tipo de servidor."
                page.update()
                return

            datos = ServidorPolicialData(
                identificacion=identificacion.value,
                nombre=nombre.value,
                grado=grado.value,
                estado=estado.value,
            )

            base_datos.actualizar_servidor(
                datos.identificacion,
                datos.nombre,
                tipo.value,
                datos.grado,
                datos.estado,
            )

            mensaje.value = (
                "Servidor actualizado correctamente."
            )

            # Actualizar tabla
            cargar_servidores()

        except ValidationError:

            mensaje.value = (
                "Error de validación. "
                "Verifique los datos ingresados."
            )

        except Exception as error:

            mensaje.value = f"Error: {error}"

        page.update()

    # ---------------------------------------------------------
    # ELIMINAR SERVIDOR
    # DELETE
    # ---------------------------------------------------------

    def eliminar_servidor(e):

        if not identificacion.value:

            mensaje.value = (
                "Ingrese la identificación del servidor."
            )

            page.update()
            return

        servidor = base_datos.buscar_servidor(
            identificacion.value
        )

        if servidor is None:

            mensaje.value = "El servidor no existe."

            page.update()
            return

        try:

            base_datos.eliminar_servidor(
                identificacion.value
            )

            mensaje.value = (
                "Servidor eliminado correctamente."
            )

            limpiar_formulario()

            # Actualizar tabla
            cargar_servidores()

        except Exception as error:

            mensaje.value = f"Error: {error}"

        page.update()

    # ---------------------------------------------------------
    # BOTONES CRUD
    # ---------------------------------------------------------

    boton_guardar = ft.Button(
        content="Guardar",
        on_click=guardar_servidor,
    )

    boton_buscar = ft.Button(
        content="Buscar",
        on_click=buscar_servidor,
    )

    boton_actualizar = ft.Button(
        content="Actualizar",
        on_click=actualizar_servidor,
    )

    boton_eliminar = ft.Button(
        content="Eliminar",
        on_click=eliminar_servidor,
    )

    botones = ft.Row(
        controls=[
            boton_guardar,
            boton_buscar,
            boton_actualizar,
            boton_eliminar,
        ],
        spacing=10,
    )

    # ---------------------------------------------------------
    # AGREGAR CONTROLES A LA INTERFAZ
    # ---------------------------------------------------------

    page.add(
        titulo,
        ft.Divider(),
        subtitulo,
        identificacion,
        nombre,
        tipo,
        grado,
        estado,
        botones,
        mensaje,
        ft.Divider(),
        ft.Text(
            "Servidores Registrados",
            size=20,
            weight=ft.FontWeight.BOLD,
        ),
        tabla_servidores,
    )

    # ---------------------------------------------------------
    # CARGAR DATOS AL INICIAR
    # ---------------------------------------------------------

    cargar_servidores()

    page.update()


ft.run(main)
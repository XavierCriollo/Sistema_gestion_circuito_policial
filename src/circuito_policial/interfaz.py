import flet as ft
from pydantic import ValidationError
from circuito_policial.validaciones import ServidorPolicialData
from circuito_policial.base_datos import BaseDatos

def main(page: ft.Page):
    
    base_datos = BaseDatos()
    base_datos.crear_tabla_servidores()
    
    # Configuración de la ventana
    page.title = "Sistema de Gestión de Circuito Policial"
    page.padding = 30

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

    # Campos del formulario
    identificacion = ft.TextField(
        label="Identificación",
        width=400,
    )

    nombre = ft.TextField(
        label="Nombre completo",
        width=400,
    )

    tipo = ft.Dropdown(
        label="Tipo de servidor",
        width=400,
        options=[
            ft.DropdownOption("Directivo"),
            ft.DropdownOption("TecnicoOperativo"),
        ],
    )

    grado = ft.TextField(
        label="Grado",
        width=400,
    )

    estado = ft.Dropdown(
        label="Estado",
        width=400,
        options=[
            ft.DropdownOption("Disponible"),
            ft.DropdownOption("Servicio"),
        ],
    )

    mensaje = ft.Text("")
    
        # Evento del botón Guardar
    def guardar_servidor(e):
        try:
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

            identificacion.value = ""
            nombre.value = ""
            tipo.value = None
            grado.value = ""
            estado.value = None

            page.update()

        except ValidationError:
            mensaje.value = "Los datos ingresados no son válidos."
            page.update()

    # Botón GUARDAR
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
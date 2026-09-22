from circuito_policial.vehiculo import Vehiculo
from circuito_policial.turno import Turno
from circuito_policial.subcircuito import Subcircuito
from circuito_policial.directivo import Directivo
from circuito_policial.tecnico_operativo import TecnicoOperativo
from circuito_policial.catalogo_servidores import CatalogoServidores
from circuito_policial.base_datos import BaseDatos

# --------------------------------------------------
# SERVIDOR POLICIAL - DIRECTIVO
# --------------------------------------------------

policia1 = Directivo(
    "Luis Criollo",
    "JC",
    "Capitan",
    "Disponible"
)

print("\n--- Información del Servidor Policial ---")
print("Nombre:", policia1.get_nombre())
print("Identificación:", policia1.get_identificacion())
print("Grado:", policia1.get_grado())
print("Estado:", policia1.get_estado())


# Cambio de estado del servidor policial

print("\n--- Cambio de estado del Servidor Policial ---")

policia1.set_estado("Servicio")

print("Nuevo estado:", policia1.get_estado())


# --------------------------------------------------
# VEHÍCULO
# --------------------------------------------------

vehiculo1 = Vehiculo(
    "V001",
    "LEA1831",
    "KIA SPORTAGE",
    "Disponible"
)

print("\n--- Información del Vehículo ---")
print("Código:", vehiculo1.get_codigo())
print("Placa:", vehiculo1.get_placa())
print("Modelo:", vehiculo1.get_modelo())
print("Estado:", vehiculo1.get_estado())


# Cambio de estado del vehículo

print("\n--- Cambio de estado del Vehículo ---")

vehiculo1.set_estado("Mantenimiento")

print("Nuevo estado:", vehiculo1.get_estado())


# --------------------------------------------------
# TURNOS DE SERVICIO
# --------------------------------------------------

print("\n--- Turno de servicio ---")

policia2 = TecnicoOperativo(
    "David Pambi",
    "CJC001",
    "Policia",
    "Disponible"
)

turno1 = Turno("Turno 1", "06:00", "13:00")
turno2 = Turno("Turno 2", "13:00", "21:00")
turno3 = Turno("Turno 3", "21:00", "06:00")
turno4 = Turno("Turno Extra", "13:00", "18:00")

turno1.agregar_servidor(policia1)
turno1.agregar_servidor(policia2)

turno1.mostrar_servidores()


# --------------------------------------------------
# SUBCIRCUITO
# --------------------------------------------------

subcircuito1 = Subcircuito(
    "Subcircuito 1",
    vehiculo1
)

subcircuito1.agregar_turno(turno1)
subcircuito1.agregar_turno(turno2)
subcircuito1.agregar_turno(turno3)

# Prueba del límite máximo de turnos
subcircuito1.agregar_turno(turno4)

print("\n--- Información del Subcircuito ---")
print("Subcircuito:", subcircuito1.get_nombre())
print("Placa:", subcircuito1.get_vehiculo().get_placa())
print("Vehículo:", subcircuito1.get_vehiculo().get_modelo())
print(
    "Estado vehículo:",
    subcircuito1.get_vehiculo().get_estado()
)


# --------------------------------------------------
# HERENCIA
# --------------------------------------------------

directivo1 = Directivo(
    "Carlos Andrade",
    "D001",
    "Capitan",
    "Disponible"
)

tecnico1 = TecnicoOperativo(
    "Juan Perez",
    "TO001",
    "Sargento Primero",
    "Disponible"
)

print("\n--- Directivo ---")
print("Nombre:", directivo1.get_nombre())
print("Identificación:", directivo1.get_identificacion())
print("Grado:", directivo1.get_grado())
print("Estado:", directivo1.get_estado())

print("\n--- Técnico Operativo ---")
print("Nombre:", tecnico1.get_nombre())
print("Identificación:", tecnico1.get_identificacion())
print("Grado:", tecnico1.get_grado())
print("Estado:", tecnico1.get_estado())


# --------------------------------------------------
# POLIMORFISMO
# --------------------------------------------------

print("\n--- Aplicación del Polimorfismo ---")

servidores = [
    directivo1,
    tecnico1
]

for servidor in servidores:
    print(
        servidor.get_grado(),
        servidor.get_nombre(),
        "-",
        servidor.mostrar_funcion()
    )
    
# --------------------------------------------------
# VALIDACIÓN CON PYDANTIC
# --------------------------------------------------

from circuito_policial.validaciones import ServidorPolicialData


print("\n--- Validación con Pydantic ---")

datos_servidor = ServidorPolicialData(
    nombre="Pedro Ramirez",
    identificacion="TO002",
    grado="Cabo Primero",
    estado="Disponible"
)

print("Nombre:", datos_servidor.nombre)
print("Identificación:", datos_servidor.identificacion)
print("Grado:", datos_servidor.grado)
print("Estado:", datos_servidor.estado)

from pydantic import ValidationError


print("\n--- Prueba de validación incorrecta ---")

try:
    datos_incorrectos = ServidorPolicialData(
        nombre="P",
        identificacion="1",
        grado="",
        estado="OK"
    )

except ValidationError as error:
    print("Pydantic detectó datos incorrectos.")
    print(error)
    
# --------------------------------------------------
# CATÁLOGO DE SERVIDORES - SEMANA 5
# --------------------------------------------------

print("\n--- Catálogo de Servidores ---")

catalogo = CatalogoServidores()

# Agregar servidores al catálogo
catalogo.agregar_servidor(directivo1)
catalogo.agregar_servidor(tecnico1)

# Prueba de identificación duplicada
catalogo.agregar_servidor(directivo1)


# --------------------------------------------------
# BUSCAR SERVIDOR
# --------------------------------------------------

print("\n--- Buscar Servidor ---")

servidor_encontrado = catalogo.buscar_servidor("D001")

if servidor_encontrado:
    print("Servidor encontrado:")
    print("Nombre:", servidor_encontrado.get_nombre())
    print("Identificación:", servidor_encontrado.get_identificacion())
    print("Grado:", servidor_encontrado.get_grado())
    print("Estado:", servidor_encontrado.get_estado())


# Prueba de búsqueda de un servidor que no existe

print("\n--- Buscar Servidor Inexistente ---")

catalogo.buscar_servidor("D999")


# --------------------------------------------------
# LISTAR SERVIDORES
# --------------------------------------------------

print("\n--- Lista de Servidores ---")

servidores_catalogo = catalogo.listar_servidores()

for servidor in servidores_catalogo:
    print(
        servidor.get_identificacion(),
        "-",
        servidor.get_nombre(),
        "-",
        servidor.get_grado(),
        "-",
        servidor.get_estado()
    )
    
# --------------------------------------------------
# ACTUALIZAR SERVIDOR
# --------------------------------------------------

print("\n--- Actualizar Servidor ---")

catalogo.actualizar_servidor(
    "TO001",
    "Juan Perez",
    "Sargento Primero",
    "Servicio"
)

servidor_actualizado = catalogo.buscar_servidor("TO001")

if servidor_actualizado:
    print("Nombre:", servidor_actualizado.get_nombre())
    print("Grado:", servidor_actualizado.get_grado())
    print("Estado:", servidor_actualizado.get_estado())


# --------------------------------------------------
# ELIMINAR SERVIDOR
# --------------------------------------------------

print("\n--- Eliminar Servidor ---")

catalogo.eliminar_servidor("D001")


# Mostrar catálogo después de eliminar

print("\n--- Lista después de eliminar ---")

for servidor in catalogo.listar_servidores():
    print(
        servidor.get_identificacion(),
        "-",
        servidor.get_nombre(),
        "-",
        servidor.get_grado(),
        "-",
        servidor.get_estado()
    )
    
# --------------------------------------------------
# PRUEBA DE ACTUALIZACIÓN CON DATOS INVÁLIDOS
# --------------------------------------------------

print("\n--- Actualización con datos inválidos ---")

catalogo.actualizar_servidor(
    "TO001",
    "J",
    "S",
    "OK"
)

print("\n--- Verificar que los datos no cambiaron ---")

servidor_verificado = catalogo.buscar_servidor("TO001")

if servidor_verificado:
    print("Nombre:", servidor_verificado.get_nombre())
    print("Grado:", servidor_verificado.get_grado())
    print("Estado:", servidor_verificado.get_estado())
    
# --------------------------------------------------
# PERSISTENCIA CON SQLITE
# --------------------------------------------------

print("\n--- Base de Datos SQLite ---")

base_datos = BaseDatos()

base_datos.crear_tabla_servidores()

print("\n--- Guardar datos de prueba en SQLite ---")

base_datos.guardar_servidor(
    "D001",
    "Carlos Andrade",
    "Directivo",
    "Capitan",
    "Disponible"
)

base_datos.guardar_servidor(
    "D002",
    "Maria Torres",
    "Directivo",
    "Teniente",
    "Servicio"
)

base_datos.guardar_servidor(
    "TO001",
    "Juan Perez",
    "TecnicoOperativo",
    "Sargento Primero",
    "Disponible"
)

base_datos.guardar_servidor(
    "TO002",
    "Pedro Ramirez",
    "TecnicoOperativo",
    "Cabo Primero",
    "Servicio"
)


print("\n--- Servidores almacenados en SQLite ---")

servidores_db = base_datos.listar_servidores()

for servidor in servidores_db:
    print(
        servidor[0],
        "-",
        servidor[1],
        "-",
        servidor[2],
        "-",
        servidor[3],
        "-",
        servidor[4]
    )
    
print("\n--- Buscar servidor en SQLite ---")

servidor_db = base_datos.buscar_servidor("TO001")

if servidor_db:
    print("Servidor encontrado:")
    print("Identificación:", servidor_db[0])
    print("Nombre:", servidor_db[1])
    print("Tipo:", servidor_db[2])
    print("Grado:", servidor_db[3])
    print("Estado:", servidor_db[4])
else:
    print("Servidor no encontrado.")
    
print("\n--- Actualizar servidor en SQLite ---")

base_datos.actualizar_servidor(
    "TO001",
    "Juan Perez",
    "TecnicoOperativo",
    "Sargento Primero",
    "Servicio"
)

print("\n--- Verificar actualización en SQLite ---")

servidor_actualizado = base_datos.buscar_servidor("TO001")

if servidor_actualizado:
    print("Identificación:", servidor_actualizado[0])
    print("Nombre:", servidor_actualizado[1])
    print("Tipo:", servidor_actualizado[2])
    print("Grado:", servidor_actualizado[3])
    print("Estado:", servidor_actualizado[4])
    
print("\n--- Eliminar servidor en SQLite ---")

base_datos.eliminar_servidor("TO002")

print("\n--- Verificar eliminación en SQLite ---")

servidor_eliminado = base_datos.buscar_servidor("TO002")

if servidor_eliminado is None:
    print("El servidor TO002 ya no existe en la base de datos.")
else:
    print("El servidor TO002 todavía existe.")
 

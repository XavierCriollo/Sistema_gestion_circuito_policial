from circuito_policial.servidor_policial import ServidorPolicial
from circuito_policial.vehiculo import Vehiculo
from circuito_policial.turno import Turno
from circuito_policial.subcircuito import Subcircuito

policia1 = ServidorPolicial(
    "Luis Criollo",
    "JC",
    "Capitan",
    "Disponible"    
)

print("\n--- Información del Servidor Policial ---")
print("Nombre: ", policia1.get_nombre())
print("Identificación: ", policia1.get_identificacion())
print("Grado: ", policia1.get_grado())
print("Estado: ", policia1.get_estado())

print("\n--- Cambio de estado ---")
policia1.set_estado("Servicio")
print("Nuevo estado: ", policia1.get_estado())

vehiculo1 = Vehiculo(
    "V001",
    "LEA1831",
    "KIA SPORTAGE",
    "Disponible"
)

print("\n--- Información del Vehículo ---")
print("Código: ", vehiculo1.get_codigo())
print("Placa: ", vehiculo1.get_placa())
print("Modelo: ", vehiculo1.get_modelo())
print("Estado: ", vehiculo1.get_estado())

print("\n--- Cambio de estado ---")
policia1.set_estado("Mantenimiento")
print("Nuevo estado: ", policia1.get_estado())

print("\n--- Turno de servicio ---")
policia2 = ServidorPolicial(
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

subcircuito1 = Subcircuito(
    "Subcircuito 1",
    vehiculo1
)

subcircuito1.agregar_turno(turno1)
subcircuito1.agregar_turno(turno2)
subcircuito1.agregar_turno(turno3)
subcircuito1.agregar_turno(turno4)

print("\n--- Información del Subcircuito ---")

print("Subcircuito:", subcircuito1.get_nombre())
print("Placa:", subcircuito1.get_vehiculo().get_placa())
print("Vehículo:", subcircuito1.get_vehiculo().get_modelo())
print("Estado vehículo:", subcircuito1.get_vehiculo().get_estado())

from circuito_policial.servidor_policial import ServidorPolicial

policia1 = ServidorPolicial(
    "Luis Criollo",
    "SP001",
    "Capitan",
    "Disponible"    
)

print("Nombre: ", policia1.get_nombre())
print("Identificacion: ", policia1.get_identificacion())
print("Grado: ", policia1.get_grado())
print("Estado: ", policia1.get_estado())

print("\n--- Cambio de estado ---")
policia1.set_estado("Servicio")
print("Nuevo estado: ", policia1.get_estado())




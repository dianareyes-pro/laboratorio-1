carnet = input("¿Tiene carnet? (si/no): ").strip().lower()
autorizacion = input("¿Tiene autorización? (si/no): ").strip().lower()

tiene_carnet = (carnet == "si")
tiene_autorizacion = (autorizacion == "si")

if tiene_carnet or tiene_autorizacion:
    print("Puede ingresar.")
else:
    print("No puede ingresar.")
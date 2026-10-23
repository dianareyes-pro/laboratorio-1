inscrito = input("¿Está inscrito? (si/no): ").strip().lower()
documento= input("¿Tiene el documento requerido? (si/no): ").strip().lower()

esta_inscrito = (inscrito == "si")
tiene_documento = (documento == "si")

if esta_inscrito and tiene_documento:
    print("Puede ingresar.")
else:
    print("No cumple todos los requisitos.")
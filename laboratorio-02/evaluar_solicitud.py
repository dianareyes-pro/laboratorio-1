edad = int(input("Ingresa tu edad: "))
inscripcion = input("¿Estás inscrito? (si/no): ").strip().lower()
documentos = int(input("Número de documentos entregados: "))

edad_valida = edad >= 16
esta_inscrito = (inscripcion == "si")
documentos_validos = documentos >= 3

if edad_valida and esta_inscrito and documentos_validos:
    print("La solicitud cumple con todos los requisitos.")
else:
    print("\nLa solicitud NO cumple con todos los requisitos. Motivos:")
    
    if not edad_valida:
        print("- Debes tener al menos 16 años.")
    if not esta_inscrito:
        print("- Debes estar inscrito.")
    if not documentos_validos:
        print("- Debes entregar al menos 3 documentos.")
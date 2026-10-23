inventario = []
opcion = ""

while opcion != "4":
    print("GESTOR DE INVENTARIO")
    print("1. Registrar nuevo producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto por código")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ").strip()
    
    if opcion == "1":
        print("Registro de Producto")
        codigo = input("Código del producto (ej. P001): ").strip()
        
        codigo_existe = False
        for producto in inventario:
            if producto["codigo"] == codigo:
                codigo_existe = True
                break
                
        if codigo_existe:
            print("Error: Ya existe un producto registrado con ese código.")
        else:
            nombre = input("Nombre del producto: ").strip()
            try:
                precio = float(input("Precio unitario: "))
                cantidad = int(input("Cantidad en stock: "))
                
                if precio < 0 or cantidad < 0:
                    print("Error: El precio y la cantidad no pueden ser negativos.")
                else:
                    nuevo_producto = {
                        "codigo": codigo,
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }
                    inventario.append(nuevo_producto)
                    print("Producto registrado exitosamente")
            except ValueError:
                print("Error: Debes ingresar valores numéricos válidos para el precio y la cantidad.")
                
    elif opcion == "2":
        print("Listado de Inventario")
        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
            for p in inventario:
                print(f"Código: {p['codigo']} | Nombre: {p['nombre']} | Precio: ${p['precio']:,.2f} | Stock: {p['cantidad']}")
                
    elif opcion == "3":
        print("Buscar Producto")
        buscado = input("Ingresa el código del producto a buscar: ").strip()
        encontrado = None
        
        for p in inventario:
            if p["codigo"] == buscado:
                encontrado = p
                break
                
        if encontrado:
            print(f"¡Producto encontrado!")
            print(f"  - Nombre: {encontrado['nombre']}")
            print(f"  - Precio: ${encontrado['precio']:,.2f}")
            print(f"  - Stock: {encontrado['cantidad']}")
        else:
            print("No se encontró ningún producto con ese código.")
            
    elif opcion == "4":
        print("Saliendo del Gestor de Inventario.")
        
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 4.")
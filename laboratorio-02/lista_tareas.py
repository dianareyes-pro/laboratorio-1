tareas = []
opcion = ""

while opcion != "0":
    print(" GESTOR DE TAREAS")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Consultar cantidad")
    print("0. Salir")
    
    opcion = input("Elige una opción: ").strip()
    
    if opcion == "1":
        nueva_tarea = input("Escribe la nueva tarea: ").strip()
        if nueva_tarea != "":
            tareas.append(nueva_tarea)
            print("Tarea agregada con éxito")
        else:
            print("La tarea no puede estar vacía.")
            
    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas registradas.")
        else:
            print("Listado de tareas:")
            for posicion, tarea in enumerate(tareas, start=1):
                print(f"{posicion}. {tarea}")
                
    elif opcion == "3":
        print("Cantidad total de tareas: {len(tareas)}")
        
    elif opcion == "0":
        print("Saliendo del gestor de tareas.")
        
    else:
        print("Opción no válida. Por favor, elige una opción del 0 al 3.")
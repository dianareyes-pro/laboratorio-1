num_notas = int(input("Ingrese el número de notas que va registrar: "))

if num_notas <= 0:
    print("El número de notas debe ser mayor que cero.")
else:
    suma_notas = 0
    for i in range(num_notas):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        suma_notas += nota

    promedio = suma_notas / num_notas
    print(f"El promedio de las notas es: {promedio}")
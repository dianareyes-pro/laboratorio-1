cantidad = int(input("¿Cuántos números deseas sumar?: "))

suma = 0

for i in range(1, cantidad + 1):
    numero = float(input(f"Ingresa el número {i}: "))
    suma += numero 

print("La suma final es:", suma)
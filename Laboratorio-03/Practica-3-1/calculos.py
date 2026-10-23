def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

resultado = calcular_subtotal(85000, 3)
print("Subtotal:", resultado)

def mostrar_total(precio, cantidad):
    print(precio * cantidad)

def obtener_total(precio, cantidad):
    return precio * cantidad

print("Probando mostrar total (efecto visible directo):")
mostrar_total(10000, 3)

print("Probando obtener total (valor devuelto para reutilizar):")
total = obtener_total(10000, 3)
print("Resultado reutilizable:", total)
def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_descuento(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)

def calcular_impuesto(base, porcentaje):
    return base * (porcentaje / 100)

subtotal = calcular_subtotal(100000, 2)
descuento = calcular_descuento(subtotal, 10)
base_despues_descuento = subtotal - descuento
impuesto = calcular_impuesto(base_despues_descuento, 19)
total = base_despues_descuento + impuesto

print(f"Subtotal: {subtotal}")
print(f"Descuento: {descuento}")
print(f"Base después del descuento: {base_despues_descuento}")
print(f"Impuesto: {impuesto}")
print(f"Total: {total}")
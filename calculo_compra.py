precio = 67000
cantidad = 8
porcentaje_descuento = 0.10

subtotal = precio * cantidad
descuento = subtotal * porcentaje_descuento
total = subtotal - descuento

print("Precio unitario: $", precio)
print("Cantidad:", cantidad)
print("Subtotal: $", subtotal)
print("Descuento: $", descuento)
print("Total: $", total)
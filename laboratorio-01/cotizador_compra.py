# Ingreso de datos
nombre = input("Ingrese su nombre: ")
producto = input("Ingrese el nombre del producto: ")
precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))
porcentaje_descuento = int(input("Ingrese el porcentaje de descuento: "))
porcentaje_impuesto = int(input("Ingrese el porcentaje de IVA: "))
costo_envio = int(input("Ingrese el costo de envío: "))
nombre_vendedor = input("Ingrese el nombre del vendedor: ")
codigo_cotizacion = int(input("Ingrese el código de cotización: "))


subtotal = precio * cantidad
valor_descuento = subtotal * (porcentaje_descuento / 100)
base_descuento = subtotal - valor_descuento


valor_impuesto = base_descuento * (porcentaje_impuesto / 100)


total_con_impuesto = base_descuento + valor_impuesto
total_final = total_con_impuesto + costo_envio


print("     RESUMEN DE COTIZACIÓN   ")
print("Código de cotización:", codigo_cotizacion)
print("Vendedor:", nombre_vendedor)
print("Cliente:", nombre)
print("Producto:", producto)
print("Precio unitario:", precio)
print("Cantidad:", cantidad)
print("Subtotal:", subtotal)
print("Descuento:", valor_descuento)
print("Base con descuento:", base_descuento)
print("Impuesto:", valor_impuesto)
print("Costo de envío:", costo_envio)
print("TOTAL FINAL:", total_final)
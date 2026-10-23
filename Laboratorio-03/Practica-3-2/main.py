#1. Primer proyecto con dos módulos 
import operaciones
subtotal = operaciones.calcular_subtotal(85000, 3)
descuento = operaciones.calcular_descuento(subtotal, 10)
print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total:", subtotal - descuento)

# 2. Importar funciones específicas ---
from operaciones import calcular_subtotal, calcular_descuento

subtotal = calcular_subtotal(40000, 2)
descuento = calcular_descuento(subtotal, 5)
print(subtotal - descuento)

# 3 y 4. Código que se ejecuta al importar y punto de entrada
import saludos
print(saludos.saludar("Laura"))

# 4. Predicción
from mensajes import despedir
print(despedir())

# 5. Separar las validaciones 
import validaciones

nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

if (
    validaciones.nombre_valido(nombre)
    and validaciones.precio_valido(precio)
    and validaciones.cantidad_valida(cantidad)
):
    print("Datos aceptados.")
else:
    print("Revisa los datos.")

import validaciones

categoria_prueba = "Componentes"
es_valida = validaciones.categoria_valida(categoria_prueba, validaciones.CATEGORIAS)
print(f"¿La categoría '{categoria_prueba}' es válida?: {es_valida}")
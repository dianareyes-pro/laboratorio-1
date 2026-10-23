from inventario import Inventario
from producto import Producto

inventario = Inventario()

p1 = Producto("P001", "Teclado")
p2 = Producto("P002", "Mouse")

print("Agregar P001:", inventario.agregar(p1))  
print("Agregar P002:", inventario.agregar(p2))  

p_repetido = Producto("P001", "Teclado Mecánico")
print("Agregar P001 repetido:", inventario.agregar(p_repetido))  

print("Eliminar P002 (existe):", inventario.eliminar("P002"))  
print(
    "Eliminar P999 (no existe):", inventario.eliminar("P999")
)  

print("\nProductos restantes en inventario:")
for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)
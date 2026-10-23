inventario = [
    {"codigo": "P001", "nombre": "Laptop", "precio": 3500000, "cantidad": 3},
    {"codigo": "P002", "nombre": "Mouse", "precio": 50000, "cantidad": 0},
    {"codigo": "P003", "nombre": "Teclado", "precio": 120000, "cantidad": 5}
]

def mostrar_productos(productos):
    print("LISTA DE PRODUCTOS")
    for p in productos:
        print(f"Código: {p['codigo']} | Nombre: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")
    print()

def buscar_producto(productos, codigo):
    for p in productos:
        if p["codigo"] == codigo:
            return p
    return None

def valor_inventario(productos):
    total = 0
    for p in productos:
        total += p["precio"] * p["cantidad"]
    return total

def productos_sin_stock(productos):
    return [p["nombre"] for p in productos if p["cantidad"] == 0]

mostrar_productos(inventario)

producto_encontrado = buscar_producto(inventario, "P003")
print(f"Búsqueda por código 'P003': {producto_encontrado}")

valor_total = valor_inventario(inventario)
print(f"Valor total del inventario: {valor_total}")

sin_stock = productos_sin_stock(inventario)
print(f"Productos sin stock: {sin_stock}")
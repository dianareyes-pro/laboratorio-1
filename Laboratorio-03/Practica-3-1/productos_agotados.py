inventario = [
    {"nombre": "Laptop", "cantidad": 5},
    {"nombre": "Mouse", "cantidad": 0},
    {"nombre": "Teclado", "cantidad": 2},
    {"nombre": "Monitor", "cantidad": 0}
]

def agotados_for(productos):
    resultado = []
    for producto in productos:
        if producto["cantidad"] == 0:
            resultado.append(producto["nombre"])
    return resultado

def agotados_comprension(productos):
    return [p["nombre"] for p in productos if p["cantidad"] == 0]

print("Agotados (con for):", agotados_for(inventario))
print("Agotados (con comprensión):", agotados_comprension(inventario))
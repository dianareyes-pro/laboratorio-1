unidades_disponibles = 12
unidades_solicitadas = 8

suficientes = unidades_solicitadas <= unidades_disponibles
iguales = unidades_solicitadas == unidades_disponibles
mas_solicitadas = unidades_solicitadas > unidades_disponibles

print("¿Hay suficientes unidades?", suficientes)
print("¿Las cantidades son iguales?", iguales)
print("¿Se solicitaron más unidades de las disponibles?", mas_solicitadas)
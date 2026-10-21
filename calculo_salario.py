nombre = "Carlos"
horas = 40
valor_hora = 25000
APORTE = 0.04

subtotal = horas * valor_hora
aporte = subtotal * APORTE
salario_neto = subtotal - aporte

print("Nombre:", nombre)
print("Horas trabajadas:", horas)
print("Valor por hora:", valor_hora)
print("Subtotal:",subtotal)
print("Aporte:", aporte)
print("Salario neto:", salario_neto)
def calcular_cobro(valor_compra, envio=10000):
    return valor_compra + envio

total_predeterminado = calcular_cobro(50000)
print(f"Total con envío predeterminado: {total_predeterminado}")

total_gratis = calcular_cobro(50000, envio=0)
print(f"Total con envío gratuito: {total_gratis}")
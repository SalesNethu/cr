def calcular_valor(valor, hora):
    return valor / hora


salario = float(input("digite o valor do salario: "))
horas = int(input("quantas horas trabalhadas por dia: "))

valor_hora = calcular_valor(salario, horas)
print(f"voce ganha {valor_hora:.2f} por hora")





    
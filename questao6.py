
numero1 = int(input("digite um numero: "))
numero2 = int(input("digite um numero: "))
operacao = str(input("""qual operação voce deseja realizar:
A - Adição
D - divisão
S - subtração
M - multiplicação
""")).upper()

resultado = 0

if operacao == "A":
    resultado = numero1 + numero2
elif operacao == "D":
    resultado = numero1 / numero2   
elif operacao == "S":
    resultado = numero1 - numero2
elif operacao == "M":
    resultado = numero1 * numero2   
else:
    print("invalido")
if resultado % 2 == 0:
    print(f"{resultado} é par")
else:
    print(f"{resultado} é ímpar")
if resultado > 0:
    print(f"{resultado} é positivo")
elif resultado < 0:
    print(f"{resultado} é negativo")
else:
    print(f"{resultado} é neutro")    
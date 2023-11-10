# def maior(n1, n2):
#     if n1 > n2:
#         return f"o maior numero é {n1}"
#     elif n2 > n1:
#         return f"o maior numero é {n2}"
#     else:
#         return "numeros iguais"
    
# numero1 = int(input("digite um numero: "))
# numero2 = int(input("digite um numero: "))

# print(maior(numero1, numero2))




def cadastro(nome, valor: float):
    return f"produto {nome} e {valor} cadastrado com sucesso "

while True:
    produto = str(input("digite o nome do produto:"))
    valor = float(input("digite o valor do produto:"))
    if produto == "sair":
        break
    print(cadastro(nome, valor))
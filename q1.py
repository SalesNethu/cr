
def imc(peso, altura):
    resultado = peso / altura **2
    return f"o imc é {resultado}"


lista_imc = []
for i in range(4):
    nome = str(input("digite o seu nome: "))
    peso = float(input("digite seu peso: "))
    altura = float(input("digite sua altura: "))
    imc1 = imc(peso, altura)
    lista_imc.append(imc1)
    print(imc1)
    


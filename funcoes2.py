# def somar_tudo(*args):
#     soma = 0
#     for item in args:
#         soma += item
#     return soma    
# somar_tudo(1,2,3,4)



# saudacao = lambda nome: f"Bom dia {nome}"
# print(saudacao("neto"))

# quadrado = lambda numero : numero **2
# print(quadrado(3))


# maior_idade = lambda idade :  "maior de idade" if idade >= 18 else "menor de idade"


# ano_de_nascimento = int(input("digite o ano do seu nascmento: "))
# idade = 2023 - ano_de_nascimento
# print(maior_idade(idade))


pos_neg = lambda numero : "positivo" if numero > 0 else "negativo" if numero < 0 else "neutro"
print(pos_neg(0))
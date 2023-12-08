#atividade1

lista_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeropar = []

def contarpar (lista_numero):
    for escolha_numero in lista_numero:
        if escolha_numero % 2 == 0:
            numeropar.append(escolha_numero)  
    return f"{numeropar} estes números são pares"  
print(contarpar(lista_numero))



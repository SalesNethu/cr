estring = lambda palavra1, palavra2 : f"{palavra1}{palavra2}" if len(palavra1) > 5 and len(palavra2) > 5 else "Erro: digitar palavras com mais de 5 letras"

nome1 = str(input("digite uma palavra: "))
nome2 = str(input("digite uma palavra: "))
print(estring(nome1, nome2))
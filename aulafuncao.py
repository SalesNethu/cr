# def maiorque(num1, num2, num3):
#      if num1 > num2 and num2 > num3:
#          return num1, "é maior"
#      elif num2 > num1 and num2 > num3:
#         return num2, "é o maior"
#      elif num3 > num1 and num3 > num2:
#          return num3, "é o maior"
#      else:
#          return "numeros iguais"
# numero1 = int(input("digite um numero: "))
# numero2 = int(input("digite um numero: ")) 
# numero3 = int(input("digite um numero: ")) 
# print(maiorque(numero1, numero2, numero3)) 

# def inverter(text0):
#     return text0[::-1]
# palavra = str(input("digite uma palavra:"))
# print(inverter(palavra))

def maior_palavra(lista_de_palavras):
        maior = ""
        for i in lista_de_palavras:
            if len(i) > len(maior):
                maior = i
        return maior           
                                                                              
lista_de_nomes = []
for i in range(5):
        nome = str(input("digite uma palavra:"))
        lista_de_nomes.append(nome)

maior = maior_palavra(lista_de_nomes)
print(f"{lista_de_nomes}a maior palavra é {maior}")                


  








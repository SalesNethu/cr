
import random
lista_participante = []
while True:
    participante = str(input("digite o nome do participante do sorteio ou SAIR para encerrar: "))
    if participante.strip().lower() == "sair":
        print("Carregando sorteio")
        break
    

    cpf = int(input("digite o seu cpf: "))



    compra = float(input("digite o valor da compra: "))

    lista_participante.append(participante)

if len(lista_participante) == 0:
    print("lista vazia, sorteio não realizado")
else:
    sorteio = (random.choice(lista_participante))
print(f"Parabéns {sorteio}, cpf: {cpf} você foi sorteado por ter feito uma compra no valor de {compra}")

    



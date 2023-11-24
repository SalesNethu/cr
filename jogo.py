import random


def zerinhoouum (jogador1, jogador2):
    if jogador1 > jogador2:
        return "jogador 1 venceu"
    elif jogador2 > jogador1:
        return "jogador 2 venceu"
    else:
        return "empate"


lista = [0, 1]  
while True:  
    jogador1 = int(input("jogador 1 digite 0 ou 1: "))
 
    if jogador1 not in lista:
        print("tente novamente entre 0 e 1: ")
    else:
        break

while True:
         
        jogador2 = int(input("jogador 2 digite 0 ou 1: "))
        if jogador2 not in lista:
            print("tente novamente entre 0 e 1: ")
        else:
            break
print(zerinhoouum(jogador1, jogador2))            


    


  
# 1. crie e a função e as opões. 

import random
def opções():
    return["pedra","papel", "tesoura"]
opções_disponíveis = opções()

# 2. mande o jogador escolher qual das opções ele quer jogar e faça o computador escolher uma opção

jogador = str(input("Escolha entre 'pedra', 'papel' ou 'tesoura' "))
computador = random.choice(opções_disponíveis)

# 3. Coloque as oções de sair e de empate

while True:
    if jogador not in opções_disponíveis:
        print("escolha inválida. Tente novamente")
        jogador = str(input("Escolha entre 'pedra', 'papel' ou 'tesoura' "))
    if jogador in opções_disponíveis:
        break 
    computador = random.choice(opçôes_disponíveis)    
# 4. bata as opções. 

if (jogador == "tesoura" and computador == "papel") or (jogador == "papel" and computador == "pedra") or (jogador == "pedra" and computador == "tesoura"):
    print("Você ganhou")
elif (jogador == "tesoura" and computador == "pedra") or (jogador == "pedra" and computador == "papel") or (jogador == "papel" and computador == "tesoura"):
    print("você perdeu")
else:
    print("empate")

print("o computador jogou:", computador)

 

# 1. o computador deve reconhecer esses itens. 

import random

def opções() :
    ["tesoura", "pedra", "papel"]

# 2. Devo pedir para o usuário escolher entre as opões pedra, papel e tesoura.

jogador = str(input("escolha entre 'pedra', 'papel' ou 'tesoura' "))
computador = random.choice(opções)   

while True:
    if jogador not in opções:
        print("Escolha inválida. Tente novamente")
    elif jogador in opções:
        break

while True: 
    elif jogador == "tesoura" and computador == "pedra" or jogador == "papel" and computador == "papel" or jogador == "papel" and computador == "tesoura":
        print("você perdeu")
    elif jogador == "tesoura" and computador == "papel" or jogador == "pedra" and computador == "tesoura" or jogador == "papel" and computador == "pedra":
        print("Voceê venceu")
    elif jogador == "tesoura" and computador == "tesoura" or jogador == "pedra" and computador == "pedra" or jogador == "papel" and computador == "papel":
        print:("empate")
    
    break
    
        

    
          



    

# 3. o computador deve saber que:
#     3.1 pedra > tesoura
#     3.2 tesoura > pepel
#     3.3 papel > pedra 
#     3.4 itens iguais a jogada se repete
# 4. o computador deve sortear um dos itens. 
# 5. as jogadas devem ser batidas e devolver o resultado ao jogador. 
import random


def checar(escolha_jogador, escolha_computador):
    if escolha_jogador == escolha_computador:
        return "empate"
    elif escolha_jogador == "pedra" and escolha_computador == "tesoura" or escolha_jogador == "papel" and escolha_computador == "pedra" or escolha_jogador == "tesoura" and escolha_computador == "papel":
        return "você venceu"
    else:
        return "o computador venceu"
    

opcoes = ["pedra", "papel", "tesoura"]
while True:
    escolha_jogador = str(input("escolha entre - pedra, papel e tesoura: ")).lower()
    print(f"você escolheu: {escolha_jogador}")
    if escolha_jogador == "sair":
        print("saindo do jogo")
        break
    elif escolha_jogador not in opcoes:
        print("escolha uma opção válida")
    else:
        escolha_computador = random.choice(opcoes)

        print(f"computador escolheu {escolha_computador}") 

        print(checar(escolha_jogador, escolha_computador))


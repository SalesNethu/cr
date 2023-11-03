cores = {"Amarelo", "Azul", "Vermelho", "Verde"}
while True:
    cor = str(input("insira uma cor: "))
    cores.add(cor)
    if cor == "sair":
        break
    print(cores)
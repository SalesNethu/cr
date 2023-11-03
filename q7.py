modulo = {"Lógica de progamação", "Python", "HTML e CSS", "Javascript"}
while True:
    newmode = str(input("insira um novo modulo: "))
    modulo.update(newmode)
    if newmode == "sair":
        break
print(modulo)    
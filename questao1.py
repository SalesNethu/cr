while True:
    nota = float(input("digite uma nota entra 0 e 10: "))
    print(nota)
    if nota <= 10 and nota >= 0:
        print("nota cadastrada com sucesso")
        break
    else:
        print("insira uma nova valida")    


def soma():
    n = int(input("digite o numero: "))
    for i in range(1, 11):
        somar = n + i
        print("{} + {} = {}".format(n, i, somar))

def subtracao():
    n = int(input("digite o numero: "))
    for i in range(1, 11):
        subtrair = i - n
        print("{} - {} = {}".format(i, n, subtrair))

def multiplicacao():
    n = int(input("digite o numero: "))
    for i in range(1, 11):
        multiplicar = n*i
        print("{} * {} = {}".format(n, i, multiplicar))

def divisao():
    n = int(input("digite o numero: "))
    for i in range(1, 11):
        dividir = i/n
        print("{} / {} = {}".format(i, n, dividir))






while True:
    menu = int(input("""Escolha a tabuada desejada: 
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    0 - Sair              
"""))                                                        
    print("a tabuada será exibida abaixo")

    match menu:
        case 1:
            soma()
        case 2:
            subtracao()
        case 3:
            multiplicacao()
        case 4:
            divisao() 
        case 0:
            print("Encerrando tabuada")  
            break
        case _:
            print("opção invalida")

            
        
                     

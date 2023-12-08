
lista_aluno = []

def cadastro (nome, cpf, turma, nota1, nota2, nota3, nota4):
    nome = str(input("digite o nome do aluno:"))
    cpf = int(input("digite o cpf do aluno: "))
    turma = str(input("digite qual a turma do aluno: "))
    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))
    nota3 = float(input("digite a terceira nota: "))
    nota4 = float(input("digite a quarta nota: "))
    aluno = {"nome" : nome,"cpf" : cpf, "turma" : turma, "nota1" : nota1, "nota2" : nota2, "nota3" : nota3, "nota4" : nota4 }
    lista_aluno.append(aluno)
 
    

def Visualizar():
    for aluno in lista_aluno():
        return 

def deletar_aluno():
    return lista_aluno.remove()
     
def sair ():
    return "encerrando o programa"     

def menu ():
    print("Menu")
    print("1 - Cadastrar Aluno")
    print("2 - Visualizar Aluno")
    print("3 - Deletar Aluno")
    print("4 - Sair")
    escolha_menu = input("Escolha uma das opções: ")

    if escolha_menu == "1":
        cadastro()
    elif escolha_menu == "2":
        Visualizar()
    elif escolha_menu == "3":
        return deletar_aluno()
    elif escolha_menu == "4":
        return sair()


    
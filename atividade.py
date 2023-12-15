lista_de_alunos = []

def adicionar_aluno ():
    nome = str(input("digite o nome do aluno:"))
    cpf = str(input("digite o cpf do aluno: "))
    turma = str(input("digite qual a turma do aluno: "))
    notas = []
    for i in range(4):
        nota = float(input("digite uma nota: "))
        notas.append(nota)
    aluno = {"nome" : nome,"cpf" : cpf, "turma" : turma, "notas" : notas }
    lista_de_alunos.append(aluno)

def visualizar_alunos():
    for aluno_atual in lista_de_alunos:
        print(f"""
    Nome do aluno: {aluno_atual["nome"]}
    CPF do aluno: {aluno_atual["cpf"]}
    Turma do Aluno: {aluno_atual["turma"]}
    Notas do aluno: {aluno_atual["notas"]}
    """)    
        
def deletar_aluno():
    visualizar_alunos()
    escolha = str(input("digite o cpf do aluno que você quer deletrar: "))
    for aluno_atual in lista_de_alunos:
        if aluno_atual["cpf"] == escolha:
            print(aluno_atual["nome"])
            posicao_na_lista = lista_de_alunos.index(aluno_atual)
            lista_de_alunos.pop(posicao_na_lista)
    print("aluno excluido com sucesso")        



while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Adicionar Aluno
    2 - Visualizar Alunos cadastrados
    3 - Delatar aluno
    0 - Sai
"""))
    
    match menu:
        case 1:
            adicionar_aluno()
        case 2:
            visualizar_alunos()
        case 3:
            deletar_aluno()
        case 0:
            break
        case _:
            print("opção invalida")
 
           
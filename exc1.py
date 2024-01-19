
alunos = []

def adicionar_aluno():
    
    matricula = int(input("digite a matricula do aluno:"))
    nome = str(input("digite o nome do aluno: "))
    aluno = {
        "Nome": nome,
        "Matrícula": matricula
    }

    for aluno in alunos:
        if aluno["Matrícula"] == matricula:
            return "Matricula já cadastrada"
        
    print(aluno)
    alunos.append(aluno)
    print("Aluno cadastrado")

    
def visualizar_alunos():
    for aluno in alunos:
        print(f"""
    Nome do aluno: {aluno['Nome']}
    Matrícula do aluno: {aluno['Matrícula']}
""")   

       

def remover_aluno():
    matricula = int(input("digite o numero da matricula do aluno a ser removido: "))

    for aluno in alunos:
        if aluno["Matrícula"] == matricula:
            alunos.remove(aluno)
            print("aluno removido com sucesso")


    
        

      
    



          

    
    

    

        
    
while True:
    menu = int(input("""
    1 - Cadastrar Aluno
    2 - Visualizar Aluno
    3 - Remover Aluno
    4 - Sair
"""))    
    match menu:
        case 1:
           adicionar_aluno()
        case 2:
            visualizar_alunos()
        case 3:
            remover_aluno()    
        case 4:
            print("saindo do programa")
            break
        case _:
            print("opção invalida, tente novamente")        
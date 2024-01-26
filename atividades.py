# class Tarefa:
#     def __init__(self, nomedatarefa:str, horaraiodatarefa:float, horariodescanso:float):
#         self.nomedatarefa = nomedatarefa
#         self.horaraiodatarefa = horaraiodatarefa
#         self.horariodescanso = horariodescanso
        

# class Projeto:
#     def __init__(self, nomeprojeto: str, priodade : str, listatarefas: list):
#         self.nomecurso = nomeprojeto
#         self.priodade = priodade
#         self.listatarefas = listatarefas



# concusrso1 = Tarefa(nomedatarefa= "estudar portugues", horaraiodatarefa= 13.30, horariodescanso= 2)
# dancar = Tarefa(nomedatarefa= "dançar", horaraiodatarefa= 18, horariodescanso= 0.15)
# caminhar = Tarefa(nomedatarefa= "caminhar", horaraiodatarefa= 6, horariodescanso= 0.30)


# projetofit = Projeto(nomeprojeto= "Projeto Fit", priodade= "alta", listatarefas=[dancar, caminhar])

# projetoconcurso = Projeto(nomeprojeto= "concusrso", priodade= "alta", listatarefas= [concusrso1])

# print(projetofit.listatarefas[0].horaraiodatarefa)
# print(projetoconcurso.listatarefas[0].nomedatarefa)




class Aluno:
    def __init__(self, nome: str, idade: int, matricula: int):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula


    def getNome(self):
        return self.__nome    
    
    def setNome(self, novo_nome):
        self.__nome = novo_nome
        return self.__nome
    
    def getIdade(self):
        return self.__idade   
    
    def setIdade(self, nova_idade):
        self.__idade = nova_idade
        return self.__idade
    

    def getMatricula(self):
        return self.__matricula 
    
    def setMatricula(self, nova_matricula):
        self.__matricula = nova_matricula
        return self.__matricula

    def visualizar(self):
        return f"""
        Nome: {self.getNome()}
        Idade: {self.getIdade()}
        Matricula: {self.getMatricula()}
"""
    

aluno1 = Aluno(nome= "joão", idade= 18, matricula= 1)
aluno2 = Aluno(nome= "Enzo", idade= 12, matricula= 20)    


print(aluno1.visualizar())
print(aluno1.getNome())
print(aluno1.setNome("Marcos"))
print(aluno1.visualizar())

print(aluno2.visualizar())
print(aluno2.getIdade())



    



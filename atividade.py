
# questão 1

# class Cachorro():
#     def __init__(self, nome:str, raça:str, idade: float ):
#         self.nome = nome
#         self.raça = raça
#         self.idade = idade


# cachorro1 = Cachorro(nome= "baleia", raça="pé duro", idade= 2 )

# print(cachorro1.nome)

# questao 2

# class Pessoa():
#     def __init__(self, nome:str, peso:float, genero: str ):
#         self.nome = nome
#         self.peso = peso
#         self.genero = genero


# pessoa1 = Pessoa(nome= "Dono do baleia", peso= 75, genero= "masculino" )

# print(pessoa1.genero)


# questao 3



class Empresa():
    def __init__(self, funcionarios: list):
        self.funcionarios = funcionarios

    def adicionar(self):
        nome1 = str(input("digite o nome do funcionário:"))
    
        cargo1 = str(input("digite o cargo do funcionário:"))
        salario1 = float(input("digite o valor do salario"))

        funcionario1 = Funcionario(nome=nome1, cargo=cargo1, salario=salario1)

        self.funcionarios.append(funcionario1)


            

class Funcionario():       
    def __init__(self, nome: str, cargo: str, salario: float):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario




while True:
    menu = int(input("""
    Selecione a opção desejada:
    1 - Adicionar Funcionarios
    2 - Remover funcionario
    3 - Listar funcionarios
"""))
    match menu:
        case 1:
            Empresa.adicionar()
            

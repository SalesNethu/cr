from datetime import datetime


class Funcionario:
    def __init__(self, nome: str, cpf: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


    def  bater_ponto(self):
        hora_atual = datetime.now().strftime("%H:%M:%S")
        
        
    
        return f"o {self.nome} bateu o ponto hoja as {hora_atual}" 
    
class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)
    def contratar(self):
        return f"o gerete {self.nome} contratou alguem"
    def demitir(self):
        return f"o gerete {self.nome} demitiu alguem"  

class Caixa(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int, numcaixa= int):
        super().__init__(nome, cpf, idade)
        self.numcaixacaixa = numcaixa         
    def fechar_caixa(self):
        hora_atual = datetime.now().strftime("%H:%M:%S")
        return f"o {self.nome} fechou o caixa as {hora_atual}"
    
    
gerente = Gerente(nome="Severo", cpf="12312312", idade= 45)
caixa = Caixa(nome="Jubiscleiton", cpf= "12123412", idade= 34, numcaixa= 5)
funcionario1 = Funcionario(nome="cleiton", cpf="1234567789", idade= 19)

print(funcionario1.bater_ponto())
print(gerente.demitir())
print(caixa.fechar_caixa())
print(gerente.contratar())




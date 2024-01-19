class Animal:
    def __init__(self, nome= str, raça= str, idade=int, cor=str):
        self.nome = nome
        self.raça = raça
        self.idade = idade
        self.cor = cor
    def emitir_som(self):
        return "som indefinido" 

class Gato(Animal):
    def __init__(self, nome=str, raça=str, idade=int, cor=str):
        super().__init__(nome, raça, idade, cor)
    def emitir_som(self):
        return "miau"
class Cachorro(Animal):
    def __init__(self, nome=str, raça=str, idade=int, cor=str):
        super().__init__(nome, raça, idade, cor)
    def emitir_som(self):
        return "auau"


gato1 = Gato(nome="frajola", raça="pe duro", idade= 2, cor="amarelo queimado")   
cachorro1 = Cachorro(nome="scoob", raça="dog alemao", idade= 50, cor="marrom")    
aranha = Animal(nome="peter", raça="super heroi", idade= 13, cor="preta")


print(cachorro1.emitir_som())
print(gato1.emitir_som())
print(aranha.emitir_som())
#herança


class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int, cor: str):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def ligar(self):
        return f"o veiculo {self.modelo} ligou"    

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, qtde_de_portas: int):
        super().__init__(marca, modelo, ano, cor)        
        self.qtde_de_portas = qtde_de_portas
    def cavalo_de_pau(self):
        return f"o carro {self.modelo} que tem {self.qtde_de_portas} portas fez um cavalo de pau"


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas: int):
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas
    def empinar(self):
        return f"a moto {self.modelo} de {self.cilindradas} cilindradas está empinando"  
    def randandandan(self):
        return f"a moto {self.modelo} está fazendo RANDANDANDAN"  



carro1 = Carro(marca= "chevrolet", modelo="celta", ano= 2010, cor="preto", qtde_de_portas= 2)
moto1 = Moto(marca= "Honda", modelo= "Twister", ano= 2010, cor="preta", cilindradas= 250)

# print(carro1.ano)
# print(moto1.cilindradas)

print(carro1.cavalo_de_pau())
print(moto1.ligar())
print(moto1.empinar())
print(moto1.randandandan())
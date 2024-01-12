# class Time:
#      def __init__(self, nome:str, anodefundacao:int, sede:str,cores:str, cidade:str, estado:str, pais:str):
#          self.nome = nome
#          self.anodefundacao = anodefundacao
#          self.sede = sede
#          self.cores = cores
#          self.cidade = cidade
#          self.estado = estado
#          self.pais = pais

      

# Time1 = Time(nome="Fortaleza", anodefundacao= 1918, sede="Pici", cores="Vermelho, azul e branco", cidade="Fortaleza", estado="Ceará", pais="Brasil")   


#  print(Time1.cores)

class Moto:
     def __init__(self, marca:str, cor:str, modelo:str, cilindradas:int ):
         self.marca = marca
         self.cor = cor
         self.modelo = modelo
         self.cilindradas = cilindradas
     def ligar(self):
        return f"A moto {self.modelo} ligou"
     def ver_informacoes(self):
         return f"""
         Marca: {self.marca}
         Modelo: {self.modelo}
         Cilindradas: {self.cilindradas}
         Cor: {self.cor}
    """
                 
moto1 = Moto(marca="honda", cor="preta", modelo="fan", cilindradas= 125 )     
moto2 = Moto(marca="dafra", cor="amarela", modelo="cansas", cilindradas= 150)   
moto3 = Moto(marca="yamaha", cor="roxa", modelo="fazer", cilindradas="250")


print(f"""
       Marca da primeira moto: {moto1.marca}.
       Cilindradas da segunda moto: {moto2.cilindradas}
       Cor da terceira moto: {moto3.cor}
""")

 
print(moto1.ligar())

print(moto2.ligar())

print(moto3.ligar())

print(moto1.ver_informacoes())
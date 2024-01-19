# crie uma classe chamda GATO que tem os atributos:
# nome, raça, peso(float), idade (int), castrado (bool)

# tenha o metodo:
# miar() que retorna uma msg dizendo:
# "o {nome do gato} está miando. dê atenção para ele"
# Instancie 2 gatos e use o metado para todos



class Gato:
    def __init__(self, nome, raça, peso=float, idade=int, castrado=bool):
        self.nome = nome
        self.raça = raça
        self.peso = peso
        self.idade = idade
        self.castrado = castrado
    def miar(self, nome):
        print(f"o {nome} está miando, dê atenção para ele")

gato1 = Gato(nome = "Seu gereba", raça = "Pé duro", peso= 3.0, idade = 4, castrado= "True")      
gato2 = Gato(nome = "fumaça", raça = "Pé duro", peso= 1.5, idade = 3, castrado= "False")   

gato1.miar(gato1.nome)



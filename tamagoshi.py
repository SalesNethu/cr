class Tamagoshi:
    def __init__(self, nome:str, especie:str, energia:int):
        self.nome = nome
        self.especie = especie
       
        self.energia = energia

    def brincar(self):
        if self.energia >= 5:
            self.energia = self.energia - 5
        else:
            print("Chico com fome")    
        return self.energia
    

    def comer(self):
        if self.energia <=95:
            self.energia = self.energia + 5
        else:
            print("Chico de barriga cheia")    
        return self.energia

tamagoshi1 = Tamagoshi(nome="chico", especie="terrestre", energia= 100)



while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Brincar
    2 - Comer
    0 - Sair
    """ ))
    match menu:
        case 1:
            tamagoshi1.brincar()
        case 2:
            tamagoshi1.comer()
        case 0:
            break    
        case _:
            print("opção invalida")
    print(f"energia atual: {tamagoshi1.energia}")                
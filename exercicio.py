#frutas = ["banana", "tamarindo", "morango", "manga", "maracuja"]
#frutas[2] = "melancia"
#print(frutas)

#frutas = ["banana", "tamarindo", "morango", "manga", "maracuja"]
#frutas.append("caju")
#print(frutas)

#frutas = ["banana", "tamarindo", "morango", "manga", "maracuja"]
#frutas.insert(2,"melancia")
#print(frutas)





# pessoas = []
# for i in range(5): 
    # pessoa = str(input("digite: "))
    # pessoas.append(pessoa)    
# print(pessoas)





# times = []
# for i in range(10):
    # time = str(input("qual time você torce: "))
    # if time == "fortaleza":
        # print("vai ser campeão da sulamericana")
    # times.append(time)
# print(times)    



pessoas = []
for i in range(5): 
    pessoa = str(input("digite um nome: "))
    pessoas.append(pessoa)  
novo_mebro = str(input("digite um novo nome:"))  
posição = int(input("em qual posição adicionar: "))
print(f"novo membro: {novo_mebro} e a posição: {posição}")  
pessoas.insert(posição -1, novo_mebro)
print(pessoas)
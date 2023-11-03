#alunos = []
#while True:
#    nome = str(input("digite o nome do aluno: "))
#    print(nome)
#    if nome == "fim":
#        break
#    nota = float(input("digite a nota do aluno: "))
#    print(nota)
#    alunos.append([nome, nota])

#maiornota = 0
#melhoraluno = ""
#for aluno in alunos:
#    if aluno[1] > maiornota:
#        maiornota = aluno[1]
#        melhoraluno = aluno[0]
#print(f"o melhor aluno foi: {melhoraluno}, com a nota {maiornota}")        

    

#pessoa = ["abel", 28, 1.79, True, 35]

#pessoa_dicionario = {
#    "nome" : "abel",
#    "idade" : 28,
#    "altura" : 1.79,
#    "acedentado" : True,
#       }
#print(pessoa_dicionario["altura"])

#forma 2
#pessoadicionario2 = dict([("nome", "abel"),("idade", 28)])

#pessoadicionario3 = dict(nome = "abel", idade = 28)

#animal = {
#    "especie" : "cachorro",
#    "Raça" : "Pinscher",
#    "idade" : 3,
#    "adestrado" : "sim"
#    }
#del animal["idade"]
#print(animal)

#frutas = ["maça", "melancia", "laranja", "morango"]
#print(dict.fromkeys(frutas))


#pc1 = {
#    "Processador": "I7",
#    "Memoria": "16GB", 
#    "SSD": "256GB"}

#print(pc1.get("Processador"))


# animal = {
#     "especie" : "cachorro",
#     "Raça" : "Pinscher",
#     "idade" : 3,
#     "adestrado" : "sim"
#     }
# animal.update({
#     "especie" : "gato",
#     "Raça" : "pé duro",
#     "idade" : 4})
# print(animal)
# #print(animal.items())
# print(animal.keys())
# print(animal.values())
# print(animal.pop("tamanho", "item não encontrado"))





frutas = {"maça","goiaba","tamarindo"}

frutas.update({"uva", "acerola"})
frutas.add("pitanga")
print(frutas)
while True:
    nome = str(input("digite seu nome:"))
    if len(nome) > 3:
        print(f"seu nome: {nome}")
        break
    else: 
        print("insira um nome maior que 3 caracteres")
while True:
    idade = int(input("digite a sua idade:"))
    if idade >= 0 and idade <= 150:
        print(f"sua idade: {idade}")
        break
    else:
        print("digite uma idade entre 0 e 150")
while True:
    salario = float(input("digite o valor do seu salario: "))    
    if salario >= 0:
        print(f"seu salario: {salario}")
        break
    else:
        print("insira um valor de salario maior que 0. ")
while True:
    sexo = str(input("qual o seu sexo: "))
    if sexo in "mM":
        print("Masculino")
        break
    if sexo in "Ff":
        print("sexo feminino")
        break
    else:
        print("tente um sexo valido")
while True:
    estado_civil = str(input("digite seu estado civil: "))
    if estado_civil in "cC":
        print("casado")
        break
    if estado_civil in "sS":
        print("solteiro")
        break    
    if estado_civil in "vV":
        print("viuvo")
        break
    if estado_civil in "dD":
        print("divorciado")
        break
    else:
        print(" tente uma das opções validas.")
print(f(nome), (idade), (salario),(sexo), (estado_civil))

    
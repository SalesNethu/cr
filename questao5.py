nota1 = float(input("nota parcial: "))
nota2 = float(input("nota bimestral: "))
media = (nota1 + nota2) / 2
print(media)
if media== 10:
    print("aprovado com distinção")
elif 7 <= media < 10 :
    print("aprovado")
else:
    print("reprovado")


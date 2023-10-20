nota1 = float(input("digite uma nota 1:"))
nota2 = float(input("digite uma nota 2:"))
nota3 = float(input("digite uma nota 3:"))
nota4 = float(input("digite uma nota 4:"))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"sua nota é {media}")  
if media == 10:
    print("APROVADO COM DISTINÇÃO")
elif media >= 7 and media < 10:
    print("APROVADO")
elif media < 7 and media > 0:
    print("REPROVADO")    
else:
    print("NOTA INVALIDA")        
   
         
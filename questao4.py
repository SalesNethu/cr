alfabeto = str(input("digite uma letra:"))
if alfabeto in "aeiouAEIOU":
    print(f"{alfabeto} é uma vogal!")
elif alfabeto in "bcdfghjklmnpqrstvxyzwBCDFGHJKLMNPQRSTVXZWY":
    print(f"{alfabeto} é um consoante")
else:
    print("digite uma letra do alfabeto")       
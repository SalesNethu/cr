frutas = {
    "fruta":"banana",
    "fruta 2" : "maça",
    "fruta 3" : "acerola",
     "fruta 4" : "pitomba"}

print(f"o dicionario possui {len(frutas)} chaves")


lista_chaves = list(frutas)
for chaves in lista_chaves:
    print(chaves)
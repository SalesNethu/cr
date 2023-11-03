lista = ["Banda", "Musica"]
dicionario = dict.fromkeys(lista)
dicionario["Banda"] = "iron Maden"
dicionario["Musica"] = "Powerslave"
print(dicionario.get("Banda", "Banda não existe"))
print(dicionario.get("Integrantes", "Integrantes não existe"))



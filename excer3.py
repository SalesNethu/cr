carro = {
    "Marca": "Ford",
    "Modelo": "Ka", 
    "Ano": 2020,
    "Cor": "Cinza"}

if "Cor" in carro:
    carro["Cor"] = "preto"
else:
    del carro["Ano"]
print(carro)
    

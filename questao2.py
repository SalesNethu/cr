while True:
    usuario = str(input("digite o nome de usuario: "))
    print(f"seu usuario é {usuario} ")
    senha = str(input("digite uma senha: "))
    if senha in usuario:
        print(" senha não pode ser igual ao usuario")
    else:
        print("usuario cadastrado com sucesso")
        break    
#while True:
#    senha = str(input("digite uma senha valida: "))
#    if len (senha) > 8:
#        print("senha valida")
#        break
#    else:
#        print("senha invalida")

while True:
    senha = str(input("digite uma senha valida: "))
    if len (senha) < 8:
        print("senha invalida, digite uma senha valida")
    else:
        print("senha valida")
        break
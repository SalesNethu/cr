while True:
    tem_letra = False
    tem_numero = False
    tem_caracteres = True
    senha = str(input("digite uma senha que tenha pelo menos 1 letra e 1 numero e maior que 8 digitos: "))
    for letra in senha:
        if letra in "0123456789":
            tem_numero = True
        elif letra in "abcdefghijklmnopqrstuvxzwy":
            tem_letra = True
        elif letra not in "!@#$%¨&*+":
            tem_caracteres = False    
    if tem_letra == True and tem_numero == True and tem_caracteres == False and len(senha) >= 9:
        print("senha valida")
        break
    else:
        print("senha invalida")        
   
     
  


   
#par ou impar

def checar_resultado():
    imparoupar1 = int(input("digite um numero:"))
    imparooupar2 = int(input("digite um numero:"))
    

while True:
    escolha1 = str(input("escolha impar ou par ou sair para encerrar:")).upper()
    if escolha1 == "sair":
        break
    elif escolha1 == "impar" or escolha1 == "par":
        print("escolha registrada")
    else: 
        print("escolha impar ou par ou sair para encerrar") 
          
        

def contador(letras):
    conta1 = 0
    conta2 = 0
    conta3 = 0
    conta4 = 0
    if " " in coisa.strip():
        for i in coisa:
            if i == " ":
                conta1 += 1
            
            elif i in "!@#$%¨&*()_+/*-+.":
                conta2 += 1
            elif i.lower() in "abcdefghijklmnopqrstuvxz":
                conta4 += 1
            elif i in "1234567890":
                conta3 += 1
        return f"a frase tem {conta4} caracteres, {conta1} espaço, {conta2} caracteres especiais e {conta3} numeros"
    else:
        return f"a palavra:'{coisa} tem {len(coisa.strip())} caracteres " 

coisa = str(input("digite uma palavra ou uma frase:"))
print(contador(coisa))
            


 
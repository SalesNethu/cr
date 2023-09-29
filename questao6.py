numero1 = int(input("digite um numero: "))
numero2 = int(input("digite um numero: "))
numero3 = int(input("digite um numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"o numero maior é:{numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"o numero maior é:{numero2}")    
else:
    print(f"o numero maior é: {numero3}")

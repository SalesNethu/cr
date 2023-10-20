#sexo = str(input("digite qual o seu sexo:"))
#if sexo in "fF":
#    print("sexo feminino")
#if sexo in "Mm":
#    print("sexo masculino")
#else:
#    print("sexo invalido")    


#sexo = str(input("digite qual o seu sexo [M / F]: "))
#if sexo in "F":
#    print("sexo feminino")
#if sexo in "M":
#    print("sexo masculino")
#else:
#    print("sexo invalido")



sexo = str(input("""digite qual o seu sexo:
F - femino
M - masculino
""")).upper().strip()

if sexo == "F":
    print("faminino")
elif sexo == "M":
    print("masculino")
else:
    print("sexo invalido")        